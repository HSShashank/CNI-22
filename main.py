import pandas as pd
from src.predict import EstimatedTravelTime
from src.evaluation import evaluate_performance

def main():
    # Load dataset
    print("Loading dataset...")
    df = pd.read_parquet('data/BMTC.parquet.gzip', engine='pyarrow')
    dfInput = pd.read_csv('data/Input.csv', index_col="Unnamed: 0")
    dfGroundTruth = pd.read_csv('data/GroundTruth.csv', index_col="Unnamed: 0")

    # Estimate travel time
    print("Estimating travel time...")
    dfOutput = EstimatedTravelTime(df, dfInput)

    # Evaluate performance
    print("Evaluating performance...")
    evaluate_performance(dfOutput, dfGroundTruth)

    # Save dfOutput as CSV
    # Convert the NumPy array to a pandas DataFrame
    dfOutput = pd.DataFrame(dfOutput)

    # Save dfOutput as CSV
    output_file = 'output/Output.csv'
    dfOutput.to_csv(output_file, index=False)
    print(f"dfOutput saved as {output_file}")

if __name__ == '__main__':
    main()
