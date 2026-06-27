import asyncio

async def teach_cognee():
    print("Teaching Cognee some engineering facts")
    await cognee.remember(
        "Gujarat Technological University offers a Bachelor of Engineering in Computer Engineering."
    )
    await cognee.remember(
        "First-year engineering students learn programming core concepts step-by-step."
    )

if __name__ == "__main__":
    asyncio.run(teach_cognee())