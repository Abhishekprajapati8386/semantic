import cohere

import gradio as gr

co = cohere.Client('mUfW6WL6RvcFah5HphHw5fzLmDPnKSHmjECAgQHe')

def write_post(topic):
  response = co.generate(
  model='command-xlarge-20221108',
  prompt=f'Create a Blogpost for \"{topic}\":',
  max_tokens=300,
  temperature=0.9,
  k=0,
  p=0.75,
  frequency_penalty=0,
  presence_penalty=0,
  stop_sequences=[],
  return_likelihoods='NONE')
  return(response.generations[0].text)

def write_email(text):
  response = co.generate(
  model='command-xlarge-20221108',
  prompt=f'Command:\"{text}\"\n Email:',
  max_tokens=200,
  temperature=0.6,
  k=0,
  p=0.75,
  frequency_penalty=0,
  presence_penalty=0,
  stop_sequences=[],
  return_likelihoods='NONE')
  return(response.generations[0].text)

def gen_hastags(hash):
  response = co.generate(
  model='command-xlarge-20221108',
  prompt=f'Post:\"{hash}"\n Hashtag:',
  max_tokens=200,
  temperature=0.3,
  k=0,
  p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop_sequences=[],
  return_likelihoods='NONE')
  return(response.generations[0].text)

with gr.Blocks() as demo:
  gr.Markdown("# FIND  BLOGPOST, E-MAILS, HASHTAGS")
  with gr.Tab("BLOGPOST"):
      gr.Markdown("# Get Blogpost")
      with gr.Row():
          blg_inp = gr.Textbox(placeholder="Enter your Topic for Blog post Generation", label="Topic")
          blg_out = gr.Textbox()
      blg_btn = gr.Button("Generate  🚀")
      blg_btn.click(fn=write_post, inputs=blg_inp, outputs=blg_out)
      
  with gr.Tab("E-mails"):
      gr.Markdown("# Get Emails for You")
      with gr.Row():
          mail_inp = gr.Textbox(placeholder="Enter for what you want to generate Email", label = "Topic")
          mail_out = gr.Textbox()
      mail_btn = gr.Button("Generate  🚀")
      mail_btn.click(fn=write_email, inputs=mail_inp, outputs=mail_out)

  with gr.Tab("HASGTAGS"):
      gr.Markdown("# Get Social Media Hastags")
      with gr.Row():
          hash_inp = gr.Textbox(placeholder="Enter your post to generate blogpost", label="Topic")
          hash_out = gr.Textbox()
      hash_btn = gr.Button("Generate  🚀")
      hash_btn.click(fn=gen_hastags, inputs=hash_inp, outputs=hash_out)
  
demo.launch()
