# coding: utf-8
import datetime

from gcms.handler.base import APIBaseHandler, handler
from gcms.model.card import CardCategory, Price
from gcms.utils.exception import ServerError


class Card(APIBaseHandler):
    def get(self):
        pass

    def post(self, *args, **kwargs):
        pass

    def put(self):
        pass

    def delete(self, *args, **kwargs):
        pass


class CardCategoryHandler(APIBaseHandler):
    @handler
    def get(self):
        card_category_id = self.argument('card_category_id', allow_null=True)
        if card_category_id:
            res = self.get_one(card_category_id)
        else:
            res = self.get_all()
        return res

    def get_one(self, card_category_id):
        cc = self.model.first(CardCategory, id=card_category_id)
        res = self.get_one_cc(cc)
        return res

    def get_all(self):
        card_categories = self.model.all(CardCategory)

        result = []
        for cc in card_categories:
            result.append(self.get_one_cc(cc))
        return result

    def get_one_cc(self, cc):
        price_list = self.model.filter_all(Price, card_category_id=cc.id)
        res = {
            'card_category_id': cc.id,
            'name': cc.name,
            'card_type': cc.card_type,
            'place_id': cc.place_id,  # TODO
            'brand_id': cc.brand_id,  # TODO
            'priority': cc.priority,
            'desc': cc.desc,
            'price': [{
                  'counts': price.counts,
                  'paid': price.paid,
                  'expire': price.expire,
                  'desc': price.desc,
                  'operate_user': '',  # TODO
                  'create_time': price.create_time,
                  'support_type': price.support_type,
              } for price in price_list]
        }
        return res

    @handler
    def post(self):
        name = self.argument('name')
        card_type = self.argument('card_type')
        place_id = self.argument('place_id')
        brand_id = self.argument('brand_id')
        priority = self.argument('priority', allow_null=True)
        desc = self.argument('desc', allow_null=True)

        cc = CardCategory(name=name, card_type=card_type, place_id=place_id, brand_id=brand_id, priority=priority,
                          desc=desc)
        self.model.add(cc)
        res = {
            'card_category_id': cc.id
        }
        return res

    @handler
    def put(self):
        card_category_id = self.argument('card_category_id')
        name = self.argument('name')
        card_type = self.argument('card_type')
        priority = self.argument('priority', allow_null=True)
        desc = self.argument('desc', allow_null=True)

        cc = self.model.first(CardCategory, id=card_category_id)
        if not cc:
            raise ServerError(ServerError.OBJECT_NOT_EXIST, ob='card_category', id=cc.id)

        cc.name = name
        cc.card_type = card_type
        cc.priority = priority
        cc.desc = desc
        self.model.commit()


class PriceHandler(APIBaseHandler):
    @handler
    def get(self):
        pass

    @handler
    def post(self):
        counts = self.argument('counts')
        paid = self.argument('paid')
        expire = self.argument('expire')
        card_category_id = self.argument('card_category_id')
        desc = self.argument('desc', allow_null=True)
        support_type = self.argument('support_type')
        create_time = datetime.datetime.now()
        price = Price(counts=counts, paid=paid, expire=expire, card_category_id=card_category_id, desc=desc,
                      support_type=support_type, create_time=create_time, update_time=create_time)
        self.model.add(price)
        res = {
            'price_id': price.id
        }
        return res

    @handler
    def put(self):
        price_id = self.argument('price_id')
        counts = self.argument('counts')
        paid = self.argument('paid')
        expire = self.argument('expire')
        card_category_id = self.argument('card_category_id')
        desc = self.argument('desc', allow_null=True)
        support_type = self.argument('support_type')
        update_time = datetime.datetime.now()

        price = self.model.first(Price, id=price_id)
        if not price:
            raise ServerError(ServerError.OBJECT_NOT_EXIST, ob='price', args=price_id)

        price.counts = counts
        price.paid = paid
        price.expire = expire
        price.card_category_id = card_category_id
        price.desc = desc
        price.support_type = support_type
        price.update_time = update_time
        self.model.commit()
