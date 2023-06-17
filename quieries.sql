SELECT "shopapp_product"."id", "shopapp_product"."name", "shopapp_product"."description", "shopapp_product"."price", "shopapp_product"."discount", "shopapp_product"."created_ad", "shopapp_product"."created_by_id", "shopapp_product"."archived", "shopapp_product"."preview" FROM "shopapp_product" WHERE NOT "shopapp_product"."archived" ORDER BY "shopapp_product"."name" ASC, "shopapp_product"."price" ASC; args=(); alias=default






