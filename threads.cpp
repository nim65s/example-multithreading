#include <iostream>
#include <mutex>
#include <thread>
#include <vector>

std::mutex cout_mutex;

auto f(int a) {
  std::lock_guard<std::mutex> lock(cout_mutex);
  std::cout << a << std::endl;
}

auto main() -> int {
  std::vector<std::thread> v;
  for (int i{0}; i < 10; i++) {
    v.push_back(std::thread(f, i));
  };
  for (auto &t : v) {
    t.join();
  }
  return EXIT_SUCCESS;
}
