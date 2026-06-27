import asyncio
import cognee

async def main():
    # 1. Give the AI memory some textbook facts to remember
    print("🧠 Teaching Cognee some biology facts...")
    await cognee.remember(
        "Mitochondria are known as the powerhouses of the cell because they generate ATP."
    )
    await cognee.remember(
        "ATP stands for Adenosine Triphosphate, which cells use as chemical energy."
    )

    # 2. Tell Cognee to process and link these facts together
    print("⚙️ Processing memory connections...")
    await cognee.cognify()

    # 3. Ask a question that requires connecting those dots
    print("🔍 Asking Cognee a question...")
    search_results = await cognee.recall("Why are mitochondria called powerhouses?")
    
    print("\n--- Cognee's Answer ---")
    print(search_results)

if __name__ == "__main__":
    asyncio.run(main())