import streamlit as st

# Loan calculator function
def loan_calculator(principal, monthly_interest_rate, term_months):
    simple_interest = principal * monthly_interest_rate * term_months
    total_simple = principal + simple_interest
    compound_total = principal * ((1 + monthly_interest_rate) ** term_months)
    compound_interest = compound_total - principal

    return {
        "Principal": f"₱{principal:,.2f}",
        "Monthly Interest Rate": f"{monthly_interest_rate * 100:.2f}%",
        "Term (months)": term_months,
        "Simple Interest": f"₱{simple_interest:,.2f}",
        "Total (Simple)": f"₱{total_simple:,.2f}",
        "Compound Interest": f"₱{compound_interest:,.2f}",
        "Total (Compound)": f"₱{compound_total:,.2f}"
    }

# Streamlit App UI
st.title("📱 Loan Calculator: Simple vs Compound Interest")

principal = st.number_input("Loan Amount (₱)", min_value=0, value=100000, step=1000)
interest_rate = st.number_input("Monthly Interest Rate (%)", min_value=0.0, value=6.0, step=0.1) / 100
term = st.number_input("Loan Term (months)", min_value=1, value=6, step=1)

if st.button("Calculate"):
    result = loan_calculator(principal, interest_rate, term)
    st.subheader("🧮 Result")
    for key, value in result.items():
        st.write(f"**{key}:** {value}")
