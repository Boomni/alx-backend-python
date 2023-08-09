async def result():
    result = []
    async for i in list(1, 2, 3):
        if i % 2:
            result.append(i)
