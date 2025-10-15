from solutions.CHK.checkout_solution import CheckoutSolution


class TestCheckout():
    # def test_checkout_wrong_item(self):
    #     assert CheckoutSolution().checkout('AZ') == -1

    # def test_checkout_no_item(self):
    #     assert CheckoutSolution().checkout('') == 0

    # def test_checkout_no_discount(self):
    #     assert CheckoutSolution().checkout('ACADBD') == 180

    # def test_checkout_several_discount(self):
    #     assert CheckoutSolution().checkout('ACADAABAADBBBC') == 420


    def test_checkout_multiplebuy(self):
        assert CheckoutSolution().checkout('AAAAA') == 200