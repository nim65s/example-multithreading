#include <atomic>
#include <iostream>
#include <thread>
#include <vector>

std::atomic<int> counter{0};

auto f() {
  for (int i{0}; i < 100000; i++) {
    ++counter;
  }
}

auto main() -> int {
  std::vector<std::thread> threads;

  for (int i{0}; i < 4; i++) {
    threads.emplace_back(f);
  }

  for (auto &t : threads) {
    t.join();
  };

  std::cout << "counter: " << counter << std::endl;

  return EXIT_SUCCESS;
}
