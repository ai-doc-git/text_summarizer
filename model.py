import warnings
warnings.filterwarnings('ignore')

from transformers import PegasusForConditionalGeneration, PegasusTokenizer
tokenizer = PegasusTokenizer.from_pretrained("google/pegasus-xsum")
model = PegasusForConditionalGeneration.from_pretrained("google/pegasus-xsum")

def text_summarization(text):
    """
    Function to take raw text input and generate summary.
    """
    tokens = tokenizer(text, truncation=True, padding='longest',return_tensors='pt')
    summary = model.generate(**tokens)
    output = tokenizer.decode(summary[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)
    return output