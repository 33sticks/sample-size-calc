import streamlit as st
import scipy.stats as stats
import numpy as np

def load_css():
    """Load custom CSS for styling the app."""
    st.markdown("""
        <style>
            /* Change slider color */
            .stSlider .thumb { background-color: #172636; }
            .stSlider .track { background-color: #EAE0D5; }

            /* Style number inputs */
            input[type="number"] {
                background-color: #FFFFFF;
                color: #172636;
                border-radius: 5px;
                border: 2px solid #EAE0D5;
                padding: 5px 10px;
            }

            input[type="number"]:hover {
                background-color: #EAF0F6;
            }

            input[type="number"]:focus {
                border-color: #172636;
                outline: none;
            }

            /* Styling the output/results section */
            .output-container {
                background-color: #EAF0F6;
                border-radius: 10px;
                border: 2px solid #172636;
                padding: 20px;
                margin-top: 20px;
                color: #172636;
            }
            
            /* Output header styles */
            .output-header {
                font-size: 24px;
                color: #172636;
                font-weight: bold;
            }

            /* Output text styles */
            .output-text {
                font-size: 18px;
                color: #000000;
            }

            /* Tightening the layout */
            .block-container {
                padding: 2rem 1rem; /* Adjust padding around main area and sidebar */
                max-width: 800px; /* Optional: constrain the max width for tighter layout */
            }

            /* Further reduce the maximum width of the main block container */
            .main .block-container {
                max-width: 700px;
            }

            /* Adjust sidebar width and padding */
            .css-1adrfps {
                width: 250px; /* Adjust width of sidebar */
                padding-right: 10px; /* Adjust right padding to reduce space */
            }
            
            .results-container {
                border: 2px solid #172636;  /* Dark blue border */
                border-radius: 10px;        /* Rounded corners */
                padding: 20px;              /* Padding inside the box */
                margin-top: 20px;           /* Space above the results box */
                background-color: #EAF0F6;  /* Light blueish gray background */
            }
        </style>
        """, unsafe_allow_html=True)


def calculate_sample_size(alpha, beta, p, mde):
    """Calculate sample size for each group in A/B testing."""
    z_alpha = stats.norm.ppf(1 - alpha / 2)
    z_beta = stats.norm.ppf(beta)
    n = ((z_alpha * np.sqrt(2 * p * (1 - p)) + 
          z_beta * np.sqrt(p * (1 - p) + (p + mde) * (1 - (p + mde)))) / mde) ** 2
    return int(round(n))  # Round the result to the nearest integer

def main():
    """Main function to run the Streamlit app."""
    load_css()
    st.title("A/B Test Sample Size Calculator")
    st.header('Input Parameters')

    confidence_level = st.slider("Confidence Level (%)", 90, 99, 95)
    statistical_power = st.slider("Statistical Power (%)", 70, 90, 80)
    baseline_conversion_rate = st.number_input("Baseline Conversion Rate (%)", value=5.0, min_value=0.1, max_value=20.0) / 100
    mde = st.number_input("Minimum Detectable Effect (MDE) as % of baseline", value=5.0, min_value=0.1, max_value=20.0) / 100

    alpha = 1 - (confidence_level / 100)
    beta = statistical_power / 100
    n = calculate_sample_size(alpha, beta, baseline_conversion_rate, mde)
    
    st.markdown('## Results', unsafe_allow_html=True)
    st.markdown(f"""
        <div class="results-container">
            <p><strong>Total Sample Size for Both Groups:</strong> {2 * n}</p>
            <p>🔵 <strong>Control Group:</strong> {n}</p>
            <p>🔴 <strong>Test Group:</strong> {n}</p>
        </div>
        """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
