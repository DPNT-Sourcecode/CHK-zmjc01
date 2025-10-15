
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        # 3 A cost 150 however we have special offer 130, which it will reduce the total count 20 every 3A products
        # 2 B COST 30  however we have special offer for 45, which it will reduce this 15 every 2B products

        prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10, 'G': 20, 'H': 10, 'I': 35, 'J': 60, 'K': 70, 'L': 90, 'M': 15, 'N': 40, 'O': 10, 'P': 50, 'Q': 30, 'R': 50, 'S': 20, 'T': 20, 'U': 40, 'V': 50, 'W': 20, 'X': 17, 'Y': 20, 'Z': 21}
        discount = {'A': [(5, 50), (3, 20)], 'B': [(2, 15)], 'H': [(10, 20), (5, 5)], 'K': [(2, 20)], 'P': [(5, 50)], 'Q': [(3, 10)], 'V': [(3, 20), (2, 10)]}
        free_item_offer = {'E': ('B', 2), 'F': ('F', 3), 'N': ('M', 3), 'R': ('Q', 3), 'U': ('U', 4)} # for every 2 E you get one B free
        
        group_items = ['S', 'T', 'X', 'Y', 'Z']
        group_offer_price = 45
        group_offer_quantity = 3

        total = 0

        # Handle group offer first
        group_item_count = {item: 0 for item in group_items}
        for item in skus:
            if item in group_item_count:
                group_item_count[item] += 1

        total_group_items = sum(group_item_count.values())
        group_offers = total_group_items // group_offer_quantity
        
        total += group_offers * group_offer_price


        import pdb; pdb.set_trace()
        remaining_group_items = total_group_items % group_offer_quantity
        if remaining_group_items > 0:
            # Sort items by price descending to maximize discount
            sorted_items = sorted(group_item_count.items(), key=lambda x: prices[x[0]], reverse=False)
            for item, count in sorted_items:
                if remaining_group_items == 0:
                    break
                if count > 0:
                    take = min(count, remaining_group_items)
                    total += take * prices[item]
                    remaining_group_items -= take
                    group_item_count[item] -= take      

        # Remove group items from skus for further processing
        skus = ''.join([item for item in skus if item not in group_items])      
        
        
        item_count = {}
        for item in skus:
            if item not in prices:
                return -1
            if item in item_count:
                item_count[item] += 1
            else:
                item_count[item] = 1 
    


        

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

        





