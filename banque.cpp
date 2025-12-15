#include <iostream>
#include <memory>
#include <mutex>
#include <thread>

class Compte {
private:
  std::string owner_;
  int amount_;
  std::mutex m_;

public:
  Compte(std::string owner, int amount) : owner_(owner), amount_(amount) {}

  auto transfert(std::shared_ptr<Compte> other, int amount) {
    std::lock_guard<std::mutex> lock(m_), lock_other(other->m_);
    amount_ -= amount;
    std::cout << owner_ << ": " << amount_ << std::endl;

    // std::lock_guard<std::mutex> lock_other(other->m_);
    //  Il faut acquerir tous les mutex en même temps,
    //  ou dans le même ordre
    //  ou un seul à la fois
    other->amount_ += amount;
    std::cout << other->owner_ << ": " << other->amount_ << std::endl;
  }
};

auto main() -> int {
  std::shared_ptr<Compte> a = std::make_shared<Compte>("a", 1000);
  std::shared_ptr<Compte> b = std::make_shared<Compte>("b", 1000);

  auto t1 = std::thread(&Compte::transfert, a, b, 10);
  auto t2 = std::thread(&Compte::transfert, a, b, 20);
  auto t3 = std::thread(&Compte::transfert, b, a, 30);

  t1.join();
  t2.join();
  t3.join();

  return EXIT_SUCCESS;
}
