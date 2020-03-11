# Fraud classification project

Source: https://www.kaggle.com/mlg-ulb/creditcardfraud  
Dataset: https://www.kaggle.com/mlg-ulb/creditcardfraud/download **(1)**

## Instruction

1. Clone this repository
2. Load dataset **(1)** into the cloned repository
3. Run all cells in **fraud_research.ipynb** to make the prediction model
4. Launch the Flask bot with command `python fraud_bot.py`
5. Test your web service with the deployed model

## Format of testing http-requests
There are only 30 features and, yep, they are obscured. It is highly recommended to use datasets with explicit features for your final project.

```json
{
	"v1": -0.41733978,
	"v2": 4.70005527,
	"v3": -7.52176683,
	"v4": 7.67188445,
	"v5": 0.26082124,
	"v6": -2.64669254,
	"v7": -2.85443216,
	"v8": 0.9587831,
	"v9": -4.58853589,
	"v10": -6.12071509,
	"v11": 4.54849458,
	"v12": -7.8362528,
	"v13": -0.24267477,
	"v14": -13.20250534,
	"v15": 1.0924416,
	"v16": -3.04086255,
	"v17": -3.008958,
	"v18": -0.15996695,
	"v19": 0.7880863,
	"v20": 0.83203479,
	"v21": 0.62220036,
	"v22": -0.43770833,
	"v23": -0.09035829,
	"v24": -0.74280216,
	"v25": -0.31236071,
	"v26": 0.50257498,
	"v27": 0.82139029,
	"v28": 0.37237882,
	"v29": -0.29665339,
	"v30": 0.89255043
}
```

## Testing details and software

You can use shell command `curl` to test your web service:
```shell
curl --header "Content-Type: application/json" \
     --request GET \
     --data 'PUT JSON HERE' \
     http://localhost:5000
```

`curl` command is actually very simple but a popular tool for a lightweight networking.  
Of course, there are great alternatives: `http` for example.

If you prefer to have graphical interface to test your web server, **Postman** is a great option. (https://www.postman.com/)  

There are a lot of tutorials about these software pieces.