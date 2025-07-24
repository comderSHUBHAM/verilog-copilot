try:
    from transformers import pipeline
    summarizer = pipeline("text2text-generation", model="tiiuae/falcon-7b-instruct")

    def generate_comment(verilog_block):
        prompt = f"Explain the following Verilog code:\n{verilog_block}"
        result = summarizer(prompt, max_length=100, do_sample=False)
        return result[0]['generated_text']

except ImportError:
    def generate_comment(verilog_block):
        return "[LLM unavailable] This block likely performs sequential logic."
