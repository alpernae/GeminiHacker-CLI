
# !  Set up the model
generation_config = {
  "temperature": 0.4,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 30720,
}

# ! Set up the safety settings
""""
Threshold (Google AI Studio)	    Threshold (API)	        Description
Block none	                        BLOCK_NONE	            Always show regardless of probability of unsafe content
Block few	                        BLOCK_ONLY_HIGH	        Block when high probability of unsafe content
Block some	                        BLOCK_MEDIUM_AND_ABOVE	Block when medium or high probability of unsafe content
Block most	                        BLOCK_LOW_AND_ABOVE	    Block when low, medium or high probability of unsafe content
"""

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_SEXUAL",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS",
    "threshold": "BLOCK_NONE"
  }
]
