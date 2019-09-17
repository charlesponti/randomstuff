# Semaphoreshave an internal counter that is incremented and
# decremented whenever an acquire or release class is made.
import asyncio

async def my_worker(semaphore):
  await semaphore.acquire()
  print("Successfullly acquired the semaphore")
  await asyncio.sleep(3)
  print("Releasing semaphore")
  semaphore.release()

async def main():
  my_semaphore = asyncio.Semaphore(value=3)
  await asyncio.wait([my_worker(my_semaphore), my_worker(my_semaphore), my_worker(my_semaphore)])
  print("Finished All Workers")

def go():
  loop = asyncio.get_event_loop()
  loop.run_until_complete(main())
  print("Our loop has completed")
  loop.close()

# if __name__ == "__main__":
#     main()