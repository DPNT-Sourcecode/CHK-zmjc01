from solutions.CHK.checkout_solution import CheckoutSolution


class TestCheckout():
    def test_checkout_wrong_item(self):
        assert CheckoutSolution().checkout('AZ') == -1

    def test_checkout(self):
        assert CheckoutSolution().checkout('') == 0

