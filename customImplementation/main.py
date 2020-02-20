import subprocess
import sys
import asyncio
from asyncio import create_subprocess_exec


async def run_process():
    C_SOURCE_CODE = "sample.c"
    JAVA_SOURCE_CODE = "JavaEx.java"

    proc = await create_subprocess_exec('gcc', C_SOURCE_CODE, '-o', 'sample', stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    run_code = await create_subprocess_exec('./sample', stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await proc.communicate()
    stdout, stderr = await run_code.communicate()

    print(stdout.decode(), stderr.decode())

loop = asyncio.get_event_loop()
commands = asyncio.gather(run_process())
loop.run_until_complete(commands)
