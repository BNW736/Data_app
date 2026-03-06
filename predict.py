import pandas as pd
import lightgbm as lb
import catboost as cd
import tensorflow as tf


class light():
    def clasifer(self,data,x,y):
        self.clean=data
        self.x_clean = self.clean[x].replace({',': ''}, regex=True).astype(float)
        self.y_clean = self.clean[y].replace({',': ''}, regex=True).astype(float).values.ravel()
        
    def lightgbm(self):
        
        model = lb.LGBMRegressor(
            boosting_type="gbdt",
            n_jobs=-1,
            learning_rate=0.0003,
            random_state=41,
            n_estimators=100,
            verbose=-1
        )
        model.fit(self.x_clean,self.y_clean)
        predict = model.predict(self.x_clean)
        return predict
    def catboot(self):
        model=cd.CatBoostRegressor(
                iterations=500,         
                learning_rate=0.03,       
                depth=6,                  
                verbose=100,               
                random_seed=41
            )
        model.fit(self.x_clean,self.y_clean)
        predict=model.predict(self.x_clean)
        return predict
    def tenser(self):
        model=tf.keras.Sequential([
            tf.keras.layers.Input(shape=(self.x_clean.shape[1],)), 
            tf.keras.layers.Dense(64,activation='linear'),
            tf.keras.layers.Dense(32),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(1)
        ])
        model.compile(optimizer="adam",loss="binary_crossentropy",metrics=['accuracy'])
        model.fit(self.x_clean,self.y_clean,epochs=10,verbose=1)
        predict=model.predict(self.x_clean)
        return predict
        