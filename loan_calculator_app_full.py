# Loan Calculator App with Summary, Interest-Only Option, and Detailed Tables
import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Loan calculator function with interest-only period
def loan_calculator(principal, monthly_interest_rate, term_months, start_date, interest_only_months=0, is_compound=False):
    records = []
    balance = principal
    total_interest = 0

    for month in range(1, term_months + 1):
        date = start_date + timedelta(days=30 * month)
        note = ""

        if month <= interest_only_months:
            interest = balance * monthly_interest_rate if is_compound else principal * monthly_interest_rate
            if is_compound:
                balance += interest
            total_due = interest
            note = "Interest Only"
        else:
            interest = balance * monthly_interest_rate if is_compound else principal * monthly_interest_rate
            if is_compound:
                balance += interest
                total_due = balance
            else:
                total_due = principal + (interest * (term_months - interest_only_months))

        total_interest += interest

        records.append({
            "Month": month,
            "Date": date.strftime("%Y-%m-%d"),
            "Interest (₱)": round(interest, 2),
            "Balance (₱)": round(balance if is_compound else total_due, 2),
            "Note": note
        })

    return records, round(total_interest, 2)

# Streamlit UI
st.set_page_config(page_title="Loan Calculator App", layout="centered")
st.title("📅 Loan Calculator with Interest-Only Option")

principal = st.number_input("Loan Amount (₱)", min_value=0, value=100000, step=1000)
interest_rate = st.number_input("Monthly Interest Rate (%)", min_value=0.0, value=6.0, step=0.1) / 100
term = st.number_input("Loan Term (months)", min_value=1, value=6, step=1)
interest_only = st.number_input("Interest-Only Months", min_value=0, max_value=term, value=2, step=1)
start_date = st.date_input("Start Date", datetime.today())

if st.button("Calculate Loan Schedule"):
    simple_table, simple_total_interest = loan_calculator(principal, interest_rate, term, start_date, interest_only_months=interest_only, is_compound=False)
    compound_table, compound_total_interest = loan_calculator(principal, interest_rate, term, start_date, interest_only_months=interest_only, is_compound=True)

    st.markdown("---")
    st.subheader("📊 Summary")
    st.markdown(f"**Simple Interest Total:** ₱{simple_total_interest:,.2f}")
    st.markdown(f"**Compound Interest Total:** ₱{compound_total_interest:,.2f}")
    st.markdown(f"**Total Payable (Simple):** ₱{principal + simple_total_interest:,.2f}")
    st.markdown(f"**Total Payable (Compound):** ₱{principal + compound_total_interest:,.2f}")

    st.markdown("---")
    st.subheader("📅 Simple Interest Table")
    st.dataframe(pd.DataFrame(simple_table))

    st.subheader("📈 Compound Interest Table")
    st.dataframe(pd.DataFrame(compound_table))
