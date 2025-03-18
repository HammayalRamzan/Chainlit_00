import chainlit as cl


@cl.on_message
async def main(message: cl.Message):
    response = f"You said: {message.content}"

    # Send a response back to the user
    await cl.Message(content=response).send()