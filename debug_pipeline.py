from app.services.pipeline import MeteoPipeline
import os
import sys

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_pipeline():
    pipeline = MeteoPipeline()
    # Use a dummy ID or one that exists if possible. 
    # Since we don't know for sure which IDs have data, we just test the flow.
    ids = ["30-station-meteo-toulouse-george-sand"] 
    print("Testing with IDs:", ids)
    try:
        df = pipeline.run(ids)
        print("Result DataFrame shape:", df.shape)
    except Exception as e:
        print("Error:", e)
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_pipeline()
