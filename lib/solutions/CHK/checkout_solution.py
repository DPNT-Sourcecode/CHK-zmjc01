
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        # 3 A cost 150 however we have special offer 130, which it will reduce the total count 20 every 3A products
        # 2 B COST 30  however we have special offer for 45, which it will reduce this 15 every 2B products

        prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10}
        discount = {'A': [(5, 50), (3, 20)], 'B': [(2, 15)]}
        free_item_offer = {'E': ('B', 2), 'F': ('F', 1)} # for every 2 E you get one B free
        item_count = {}
        for item in skus:
            if item not in prices:
                return -1
            if item in item_count:
                item_count[item] += 1
            else:
                item_count[item] = 1 
        total = 0



        # Apply free item first
        for item, count in item_count.items():
            if item in free_item_offer:
                    free_item, required_count = free_item_offer[item]
                    if free_item in item_count:
                        item_count[free_item] = max(0, item_count[free_item] - (count // required_count))

        # Apply discount and calculate total
        for item, count in item_count.items():
            total += count * prices[item]
            if item in discount:
                special_offers = discount[item]
                for offer in special_offers:
                    discount_count, discount_amount = offer
                    total -= (count // discount_count) * discount_amount 
                    count = count%discount_count # reduce the count for the next discount
                           
        
        return total

        


