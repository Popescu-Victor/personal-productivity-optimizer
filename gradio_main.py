import gradio as gr

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column(scale=4):
            graph_canvas = gr.Plot(label="Canvas for plotting graphs")
        with gr.Column(scale=1):
            textbox = gr.Textbox(label="Textbox", lines=20)
    with gr.Row():
        user_input = gr.Textbox(label="User text input", scale=4)
        submit_btn = gr.Button("Return", scale=1)

    def handle_input(text):
        return f"You entered: {text}"

    submit_btn.click(
        fn=handle_input,
        inputs=user_input,
        outputs=textbox
    )

demo.launch()