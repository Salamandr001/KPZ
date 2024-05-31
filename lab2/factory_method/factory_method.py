from abc import ABC, abstractmethod

# Abstract Product
class Subscription(ABC):
    def __init__(self, monthly_fee, min_period, channels, features):
        self.monthly_fee = monthly_fee
        self.min_period = min_period
        self.channels = channels
        self.features = features

    @abstractmethod
    def get_details(self):
        pass

# Concrete Products
class DomesticSubscription(Subscription):
    def get_details(self):
        return f"Domestic Subscription: {self.monthly_fee} per month, {self.min_period} months minimum, Channels: {', '.join(self.channels)}, Features: {', '.join(self.features)}"

class EducationalSubscription(Subscription):
    def get_details(self):
        return f"Educational Subscription: {self.monthly_fee} per month, {self.min_period} months minimum, Channels: {', '.join(self.channels)}, Features: {', '.join(self.features)}"

class PremiumSubscription(Subscription):
    def get_details(self):
        return f"Premium Subscription: {self.monthly_fee} per month, {self.min_period} months minimum, Channels: {', '.join(self.channels)}, Features: {', '.join(self.features)}"

# Creator
class SubscriptionCreator(ABC):
    @abstractmethod
    def create_subscription(self):
        pass

# Concrete Creators
class WebSite(SubscriptionCreator):
    def create_subscription(self, sub_type):
        if sub_type == 'domestic':
            return DomesticSubscription(10, 6, ["Channel 1", "Channel 2"], ["Feature A"])
        elif sub_type == 'educational':
            return EducationalSubscription(8, 12, ["Channel 3", "Channel 4"], ["Feature B"])
        elif sub_type == 'premium':
            return PremiumSubscription(20, 3, ["Channel 5", "Channel 6"], ["Feature C", "Feature D"])
        else:
            return None

class MobileApp(SubscriptionCreator):
    def create_subscription(self, sub_type):
        if sub_type == 'domestic':
            return DomesticSubscription(12, 6, ["Channel 1", "Channel 2", "Channel 7"], ["Feature A", "Feature E"])
        elif sub_type == 'educational':
            return EducationalSubscription(9, 12, ["Channel 3", "Channel 4", "Channel 8"], ["Feature B", "Feature F"])
        elif sub_type == 'premium':
            return PremiumSubscription(22, 3, ["Channel 5", "Channel 6", "Channel 9"], ["Feature C", "Feature D", "Feature G"])
        else:
            return None

class ManagerCall(SubscriptionCreator):
    def create_subscription(self, sub_type):
        if sub_type == 'domestic':
            return DomesticSubscription(11, 6, ["Channel 1", "Channel 2", "Channel 10"], ["Feature A", "Feature H"])
        elif sub_type == 'educational':
            return EducationalSubscription(7, 12, ["Channel 3", "Channel 4", "Channel 11"], ["Feature B", "Feature I"])
        elif sub_type == 'premium':
            return PremiumSubscription(18, 3, ["Channel 5", "Channel 6", "Channel 12"], ["Feature C", "Feature D", "Feature J"])
        else:
            return None

# Client Code
def main():
    creators = [WebSite(), MobileApp(), ManagerCall()]
    subscription_types = ['domestic', 'educational', 'premium']

    for creator in creators:
        for sub_type in subscription_types:
            subscription = creator.create_subscription(sub_type)
            print(subscription.get_details())

if __name__ == "__main__":
    main()
