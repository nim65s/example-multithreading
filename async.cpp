#include <future>
#include <iostream>

auto f(int x) -> int { return x * x; }

auto main() -> int {
  auto future = std::async(std::launch::async, f, 5);

  std::cout << future.get() << std::endl;

  return EXIT_SUCCESS;
};
