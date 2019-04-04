print("".join((lambda s: "FizzBuzz" if s%15==0 else ("Buzz" if s%5==0 else ("Fizz" if s%3==0 else str(s))))(i)+"\n" for i in range(1,101)))
