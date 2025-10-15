from solutions.CHK.checkout_solution import CheckoutSolution


class TestCheckout():
    def test_checkout(self):
        assert CheckoutSolution().compute(1, 2) == 3
