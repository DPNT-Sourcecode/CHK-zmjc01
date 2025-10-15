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


    # # Here
    # def test_checkout_wrong_item(self):
    #     # Test an illegal SKU ('Z' is valid, 'X' is valid, but 'a' is illegal lowercase)
    #     assert CheckoutSolution().checkout('AZa') == -1

    # def test_checkout_no_item(self):
    #     assert CheckoutSolution().checkout('') == 0

    # def test_checkout_no_discount(self):
    #     # Test a mix of items without discounts, including new ones (G, I, J, L, M, O, S, T, W, X, Y, Z)
    #     # ACDB: 50+20+15+30 = 115.  + G + I + J + L + M + O + S + T + W + X + Y + Z
    #     # 50+20+15+30 + 20+35+60+90+15+10+30+20+20+90+10+50 = 560
    #     assert CheckoutSolution().checkout('ACDBGIJLMOSTWXYZ') == 560

    # # --- R4: Complex Nested Multi-Buy Offers ---

    # # Item H (10): 5H for 45 (9/item), 10H for 80 (8/item) -> Maximize 10H first
    # def test_checkout_offer_h_nested(self):
    #     assert CheckoutSolution().checkout('HHHH') == 40  # 4 * 10 = 40 (below 5H threshold)
    #     assert CheckoutSolution().checkout('HHHHH') == 45  # 5H for 45
    #     assert CheckoutSolution().checkout('HHHHHHHHHH') == 80  # 10H for 80
    #     assert CheckoutSolution().checkout('HHHHHHHHHHHH') == 100  # 10H for 80 + 2H @ 10 = 100
    #     assert CheckoutSolution().checkout('HHHHHHHHHHHHHHH') == 125  # 10H for 80 + 5H for 45 = 125

    # # Item V (50): 3V for 130 (43.33/item), 2V for 90 (45/item) -> Maximize 3V first
    # def test_checkout_offer_v_nested(self):
    #     assert CheckoutSolution().checkout('VV') == 90  # 2V for 90
    #     assert CheckoutSolution().checkout('VVV') == 130  # 3V for 130
    #     assert CheckoutSolution().checkout('VVVV') == 180  # 3V for 130 + 1V @ 50 = 180
    #     assert CheckoutSolution().checkout('VVVVV') == 220  # 3V for 130 + 2V for 90 = 220

    # # --- R4: Simple Multi-Buy Offers ---

    # def test_checkout_offer_k(self):
    #     assert CheckoutSolution().checkout('K') == 80
    #     assert CheckoutSolution().checkout('KK') == 150
    #     assert CheckoutSolution().checkout('KKK') == 230  # 2K for 150 + 1K @ 80 = 230

    # def test_checkout_offer_p_q(self):
    #     assert CheckoutSolution().checkout('PPPPP') == 200  # 5P for 200
    #     assert CheckoutSolution().checkout('QQQ') == 80  # 3Q for 80
    #     assert CheckoutSolution().checkout('QQQQQ') == 140  # 3Q for 80 + 2Q @ 30 = 140

    # # --- R4: 'Buy N Get 1 Free' Offers ---

    # # Item F (10): 2F get 1F free (3 for 20)
    # def test_checkout_offer_f_buy_get_free(self):
    #     assert CheckoutSolution().checkout('FFF') == 20
    #     assert CheckoutSolution().checkout('FFFFFF') == 40

    # # Item U (40): 3U get 1U free (4 for 120)
    # def test_checkout_offer_u_buy_get_free(self):
    #     assert CheckoutSolution().checkout('UUU') == 120  # 3U @ 40 = 120 (4th U free if present)
    #     assert CheckoutSolution().checkout('UUUU') == 120  # 4U: 3 paid, 1 free. 3 * 40 = 120
    #     assert CheckoutSolution().checkout('UUUUUU') == 200 # 4U for 120 + 2U @ 40 = 200

    # # --- R4: Cross-Item Offers (N/M and R/Q) ---

    # # Item N/M: 3N get 1M free. N=40, M=15.
    # def test_checkout_offer_nm_cross_item(self):
    #     assert CheckoutSolution().checkout('NNNM') == 120    # 3N @ 40 = 120. M is free.
    #     assert CheckoutSolution().checkout('NNNMM') == 135   # 3N @ 40 = 120. 1M free. 1M charged @ 15.
    #     assert CheckoutSolution().checkout('NNNNNNMM') == 240 # 6N @ 40 = 240. 2M free. 0M charged.

    # # Item R/Q: 3R get 1Q free. R=50, Q=30.
    # def test_checkout_offer_rq_cross_item(self):
    #     assert CheckoutSolution().checkout('RRRQQ') == 180   # 3R @ 50 = 150. 1Q free. 1Q charged @ 30.
    #     assert CheckoutSolution().checkout('RRRRRRQQQQQ') == 380  # 6R @ 50 = 300. 2Q free. 3Q charged @ 80 (3Q for 80 offer).

    # # --- R4: Existing Complex Offers (for regression testing) ---

    # # Item A (50): 5A for 200 (best), 3A for 130 (second best)
    # def test_checkout_multipleoffer_same_item_a(self):
    #     assert CheckoutSolution().checkout('AAAAAAAA') == 330  # 5A for 200 + 3A for 130 = 330
    #     assert CheckoutSolution().checkout('AAAAAAAAA') == 380 # 5A for 200 + 3A for 130 + 1A @ 50 = 380

    # # Item E/B (2E get 1B free) - Must interact with B's own offer (2B for 45)
    # def test_checkout_offer_eb_cross_item(self):
    #     assert CheckoutSolution().checkout('EEEEBBBB') == 205  # 4E @ 40 = 160. 2B free. 2B charged @ 45 (2B offer).
    #     assert CheckoutSolution().checkout('EEEBB') == 150     # 3E @ 40 = 120. 1B free. 1B charged @ 30.

    # # --- Combined Scenarios ---

    # def test_checkout_complex_combination_all_offers(self):
    #     # Basket: 3A, 2B, 3N, 1M, 5H, 3Q, 3V, 3F
    #     # SKUs: AAABBNNNMHHHHHQQQVVVFFF
    #     # A: 130 (3A)
    #     # B: 45 (2B)
    #     # N: 120 (3N gives 1M free)
    #     # M: 0 (1M free)
    #     # H: 45 (5H)
    #     # Q: 80 (3Q)
    #     # V: 130 (3V)
    #     # F: 20 (3F)
    #     # Total: 130 + 45 + 120 + 0 + 45 + 80 + 130 + 20 = 570
    #     assert CheckoutSolution().checkout('AAABBNNNMHHHHHQQQVVVFFF') == 570


