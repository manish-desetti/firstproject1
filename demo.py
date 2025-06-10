from us_visa.pipline.training_pipeline import TrainPipeline
from dotenv import load_dotenv
load_dotenv() 
import warnings
warnings.filterwarnings("ignore", category=UserWarning)


#import os
#print("MONGODB_URL =", os.getenv("MONGODB_URL"))


obj=TrainPipeline()
obj.run_pipeline()