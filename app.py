# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session;
from datetime import datetime;

session = get_active_session()

def main():
    st.title("SVeN");

if __name__ == "__main__":
    main();

q_comments = f"""SELECT * FROM SVENNOTES.PUBLIC.NOTES2 ORDER BY 1 desc LIMIT 10"""
df_comments = session.sql(q_comments).to_pandas()

st.dataframe(df_comments, use_container_width=True)

date_val = st.text_input("Date", value=datetime.now().strftime("%Y-%m-%d"))
subject_val = st.text_input("Subject")
details_val = st.text_input("Details");

submitted = st.button("Save Note")
if submitted:
    session.sql(f"""INSERT INTO SVENNOTES.PUBLIC.NOTES2 (ADDDATE, SUBJECT, DETAILS)
	VALUES ('{date_val}', '{subject_val}', '{details_val}')"""
	).collect();
