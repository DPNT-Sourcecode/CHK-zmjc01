
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        # 3 A cost 150 however we have special offer 130, which it will reduce the total count 20 every 3A products
        # 2 B COST 30  however we have special offer for 45, which it will reduce this 15 every 2B products

        prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
        discount = {'A': [(5, 50), (3, 20)], 'B': [(2, 15)], 'E': [(3, 80)]}
        item_count = {}
        for item in skus:
            if item not in prices:
                return -1
            if item in item_count:
                item_count[item] += 1
            else:
                item_count[item] = 1 
        total = 0
        for item, count in item_count.items():
            total += count * prices[item]
            if item in discount:
                special_offers = discount[item]
                for offer in special_offers:
                    discount_count, discount_amount = offer
                    total -= (count // discount_count) * discount_amount 
                    count = count%discount_count # reduce the count for the next discount
                           
        
        return total

        
