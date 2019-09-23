from flask import Flask
from flask_restplus import Api

app = Flask(__name__)

api = Api(
   app, 
   version='beta - Isra', 
   title='Prediksi Pinjaman - Isra',
   description='Prediksi Penerimaan Pinjaman Kredit')

ns = api.namespace('Penerimaan Kredit', 
   description='Credit Approval')

from flask_restplus import fields
resource_fields = api.model('Resource', {
    'result': fields.String,
})

parser = api.parser()
parser.add_argument(
   'Rasio Total Tagihan dibagi Limit', 
   type=float, 
   required=True, 
   help='RevolvingUtilizationOfUnsecuredLines', 
   location='form')
parser.add_argument(
   'Usia', 
   type=float, 
   required=True, 
   help='Age of Borrower',
   location='form')
parser.add_argument(
   'Jumlah Terlambat 30-59 Hari',
   type=float, 
   required=True, 
   help='NumberOfTime30-59DaysPastDueNotWorse',
   location='form')
parser.add_argument(
   'Rasio Hutang', 
   type=float, 
   required=True, 
   help='debtRatio',
   location='form')
parser.add_argument(
   'Pendapatan per Bulan', 
   type=float, 
   required=True, 
   help='MonthlyIncome',
   location='form')
parser.add_argument(
   'Hutang Tertanggung', 
   type=float, 
   required=True, 
   help='NumberOfOpenCreditLinesAndLoans',
   location='form')
parser.add_argument(
   'Jumlah Terlambat 90 Hari', 
   type=float, 
   required=True, 
   help='NumberOfTimes90DaysLate',
   location='form')
parser.add_argument(
   'Aset Pribadi', 
   type=float, 
   required=True, 
   help='NumberRealEstateLoansOrLines',
   location='form')
parser.add_argument(
   'Jumlah Terlambat 60-89 Hari', 
   type=float, 
   required=True, 
   help='NumberOfTime60-89DaysPastDueNotWorse',
   location='form')
parser.add_argument(
   'Jumlah Tanggungan Keluarga', 
   type=float, 
   required=True, 
   help='NumberOfDependents',
   location='form')

from flask_restplus import Resource
@ns.route('/')
class CreditApi(Resource):

   @api.doc(parser=parser)
   @api.marshal_with(resource_fields)
   def post(self):
     args = parser.parse_args()
     result = self.get_result(args)

     return result, 201

   def get_result(self, args):
      debtRatio = args["Rasio Hutang"]
      monthlyIncome = args["Pendapatan per Bulan"]
      dependents = args["Jumlah Tanggungan Keluarga"]
      openCreditLinesAndLoans = args["Hutang Tertanggung"]
      pastDue30Days = args["Jumlah Terlambat 30-59 Hari"]
      pastDue60Days = args["Jumlah Terlambat 60-89 Hari"]
      pastDue90Days = args["Jumlah Terlambat 90 Hari"]
      realEstateLoansOrLines = args["Aset Pribadi"]
      unsecuredLines = args["Rasio Total Tagihan dibagi Limit"]
      age = args["Usia"] 

      from pandas import DataFrame
      df = DataFrame([[
         debtRatio,
         monthlyIncome,
         dependents,
         openCreditLinesAndLoans,
         pastDue30Days,
         pastDue60Days,
         pastDue90Days,
         realEstateLoansOrLines,
         unsecuredLines,
         age
      ]])

      from sklearn.externals import joblib
      clf = joblib.load('model.pkl');

      result = clf.predict(df)
      if(result[0] == 1.0): 
         result = "Pengajuan Kredit Pemohon Ditolak" 
      else: 
         result = "Pengajuan Kredit Pemohon Diterima"

      return {
         "result": result
      }

if __name__ == '__main__':
    app.run(debug=True)
