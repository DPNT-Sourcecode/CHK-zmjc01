from solutions.CHK.checkout_solution import CheckoutSolution


class TestCheckout():
    def test_checkout_wrong_item(self):
        assert CheckoutSolution().checkout('AZ') == -1

    def test_checkout_no_item(self):
        assert CheckoutSolution().checkout('') == 0

    def test_checkout_no_discount(self):
        assert CheckoutSolution().checkout('ACADBD') == 180

    def test_checkout_several_discount(self):
        assert CheckoutSolution().checkout('ACADAABAADBBBC') == 410


    def test_checkout_multipleoffer_same_item(self):
        assert CheckoutSolution().checkout('AAAAAAAAA') == 380

    def test_checkout_offer_free(self):
        assert CheckoutSolution().checkout('EEEEEB') == 200


    def test_checkout_offer_free_b(self):
        assert CheckoutSolution().checkout('EEEEBBBB') == 205

    def test_checkout_offer_f(self):
        assert CheckoutSolution().checkout('F') == 10
    
    def test_checkout_offer_multiple_f(self):
        assert CheckoutSolution().checkout('FF') == 20
        assert CheckoutSolution().checkout('FFF') == 20
        assert CheckoutSolution().checkout('FFFF') == 30
        assert CheckoutSolution().checkout('FFFFFF') == 40
