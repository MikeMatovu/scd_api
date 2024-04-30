from flask import Flask, jsonify, request
import joblib
import flask
import pandas as pd
from joblib import dump, load

print("Flask version: ", flask.__version__)
print("Pandas version: ", pd.__version__)
print("Joblib version: ", joblib.__version__)


app = Flask(__name__, template_folder='templates')
#CORS(app)

@app.route('/everything', methods=['POST'])
def main():

        data = request.get_json()
 
        Gender_sex = data.get('gender')
        Age_of_patient = data.get('patientAge')
        Age_at_diagnosis = data.get('diagnosisAge')
        Body_Mass_Index_BMI = data.get('bmi')
        Packet_Cell_Volume_PCV = data.get('pcv')
        Frequency_of_Anemia_Crisis = data.get('crisisFrequency')
        Frequency_of_Blood_Transfusions = data.get('transfusionFrequency')
        Peripheral_Capillary_Oxygen_Saturation_Spo2 = data.get('spo2')
        Systolic_BP = data.get('systolicBP')
        Diastolic_BP = data.get('diastolicBP')
        Heart_Rate_Pulse = data.get('heartRate')
        Respiratory_Rate_Resp = data.get('respiratoryRate')
        Hb_F = data.get('hbF')
        Temp = data.get('temp')
        Mean_corpuscular_volume_MCV = data.get('mcv')
        Platelets_PLTS = data.get('platelets')
        Alanine_Aminotransferase_ALT_test = data.get('alt')
        Bilirubin = data.get('bilirubin')
        Lactate_Dehydrogenase_LDH = data.get('ldh')
        Percentage_average = data.get('percentageAverage')
        


        input_variables = pd.DataFrame([[Gender_sex, Age_of_patient, Age_at_diagnosis, Body_Mass_Index_BMI, Packet_Cell_Volume_PCV, Frequency_of_Anemia_Crisis, Frequency_of_Blood_Transfusions, Peripheral_Capillary_Oxygen_Saturation_Spo2, Systolic_BP, Diastolic_BP, Heart_Rate_Pulse, Respiratory_Rate_Resp, Hb_F, Temp, Mean_corpuscular_volume_MCV, Platelets_PLTS, Alanine_Aminotransferase_ALT_test, Bilirubin, Lactate_Dehydrogenase_LDH, Percentage_average]],
                                       columns=['Gender (sex)', 'Age of patient', 'Age at diagnosis', 'Body Mass Index BMI', 'Packet Cell Volume (PCV)', 'Frequency of Anemia Crisis', 'Frequency of Blood Transfusions', 'Peripheral Capillary Oxygen Saturation (Spo2)', 'Systolic BP', 'Diastolic BP', 'Heart Rate (Pulse)', 'Respiratory Rate (Resp)', 'Hb F', 'Temp', 'Mean corpuscular volume (MCV)', 'Platelets (PLTS)', 'Alanine Aminotransferase (ALT) test', 'Bilirubin', 'Lactate Dehydrogenase (LDH)', 'Percentage average'],
                                    
                                       index=['input'])
        
        # model = load("model/best_model.joblib")
    
        # predictions = model.predict(input_variables)[0]
        # probabilities = model.predict_proba(input_variables)[0]
        # print(predictions)
        
        # print(probabilities)
        return jsonify({
                # 'prediction': str(predictions),
                # 'probability0': probabilities[0],
                # 'probability1': probabilities[1]
                'test': "test"
        })
        


# if __name__ == '__main__':
#     app.run(host='192.168.100.60', port=5001, debug=True)
    