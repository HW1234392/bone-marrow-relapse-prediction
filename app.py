import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model.pkl")

st.title("Pediatric Bone Marrow Transplant Relapse Prediction Model")

st.write("""
         본 웹서비스는 소아 조혈모세포 이식(Pediatric Bone Marrow Transplant) 환자의
         임상 데이터를 기반으로 재발 여부를 예측하는 인공지능 분류 모델입니다.
        
         재발은 환자의 생존율과 직접적으로 연관된 중요한 예후 지표이기 때문에
         이식 전·후에 확보된 임상 특성을 활용해 재발 가능성을 사전에 파악하는 것은
         의사들의 치료 의사결정에 큰 도움을 줄 수 있습니다.

         본 모델은 Kaggle 데이터셋(187명 소아 이식 환자)을 기반으로,
         Rank 분석을 통해 선별한 주요 8개 임상 기표만을 사용해 학습한
         'Decision Tree 기반 이진 분류 모델'입니다.
         사용자가 개별 환자의 임상 정보를 입력하면 모델이 재발 여부를 예측하여 보여줍니다.

         ※ 본 서비스는 과제 및 연구 학습용 데모이며, 실제 의료 진단에는 사용할 수 없습니다.
""")

recipient_gender = st.selectbox("수혜자의 성별(male/female)", ['male', 'female'])
recipient_AB0 = st.selectbox("수혜자의 ABO 혈액형(0, A, AB, B)", ['0', 'A', 'B', 'AB', '?'])
recipient_rh = st.selectbox("수혜자의 Rh 인자(+/-)", ['plus', 'minus'])
disease = st.selectbox("기저 질병의 종류", ['ALL', 'AML', 'chronic', 'nonmalignant', 'lymphoma'])
disease_group = st.selectbox("질병군", ['malignant', 'nonmalignant'])
risk_group = st.selectbox("수혜자 위험도 수준", ['high', 'low'])
tx_post_relapse = st.selectbox("이식 전 재발 경험 유무(yes/no)", ['yes', 'no'])
CD3_to_CD34_ratio = st.number_input("공여자 조혈모세포 내 T세포(CD3+)와 조혈모세포(CD34+) 비율", value=0.0)

if st.button("예측하기"):
    input_df = pd.DataFrame([{
        "recipient_gender": recipient_gender,
        "recipient_AB0": recipient_AB0,
        "recipient_rh": recipient_rh,
        "disease": disease,
        "disease_group": disease_group,
        "risk_group": risk_group,
        "tx_post_relapse": tx_post_relapse,
        "CD3_to_CD34_ratio": CD3_to_CD34_ratio
    }])

    pred = model.predict(input_df)[0]

    st.success(f"예측 결과: {pred}")

