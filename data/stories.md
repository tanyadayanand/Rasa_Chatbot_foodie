<!-- markdownlint-disable -->

<!-- greet, ask restaurant -->
## story_01_location_cuisine_valid_with_email
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "Bangalore"}
  - slot{"location": "Bangalore"}  
  - action_verify_location
  - slot{"location": "Bangalore"}  
  - slot{"location_ok": true}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - slot{"cuisine": "Chinese"}
  - utter_ask_price_range
* restaurant_search{"price": "Lesser than Rs. 300"}   
  - slot{"price": "Lesser than Rs. 300"}
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email
* sendmail{"email": "tanyadayanand@gmail.com"}   
  - slot{"email": "tanyadayanand@gmail.com"}
  - action_send__mail
  - slot{"email": "tanyadayanand@gmail.com"}
* thank
  - utter_goodbye
  - action_restart

## story_02_location_invalid_retry_with_email
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "Manorpur"}
  - slot{"location": "Manorpur"}  
  - action_verify_location
  - slot{"location": null}   
  - slot{"location_ok": false}     
  - action_slot_reset    
  - reset_slots    
  - utter_ask_location 
* restaurant_search{"location": "Bangalore"}
  - slot{"location": "Bangalore"}  
  - action_verify_location
  - slot{"location": "Bangalore"}  
  - slot{"location_ok": true}
  - utter_ask_cuisine  
* restaurant_search{"cuisine": "Chinese"}
  - slot{"cuisine": "Chinese"}
  - utter_ask_price_range
* restaurant_search{"price": "Lesser than Rs. 300"}   
  - slot{"price": "Lesser than Rs. 300"}
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email
* sendmail{"email": "tanyadayanand@gmail.com"}   
  - slot{"email": "tanyadayanand@gmail.com"}
  - action_send__mail
  - slot{"email": "tanyadayanand@gmail.com"}
* thank
  - utter_goodbye
  - action_restart

## story_03_location_invalid_deny
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "Bansur"}
  - slot{"location": "Bansur"}  
  - action_verify_location
  - slot{"location": null}   
  - slot{"location_ok": false}     
  - action_slot_reset    
  - reset_slots    
  - utter_ask_location 
* deny
  - utter_deny
  - utter_goodbye
  - action_restart

## story_04_location_cuisine_valid_no_email
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "Bangalore"}
  - slot{"location": "Bangalore"}  
  - action_verify_location
  - slot{"location": "Bangalore"}  
  - slot{"location_ok": true}  
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - slot{"cuisine": "Chinese"}
  - utter_ask_price_range
* restaurant_search{"price": "Lesser than Rs. 300"}   
  - slot{"price": "Lesser than Rs. 300"}
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email 
* deny
  - utter_goodbye
  - action_restart

## story_05_location_happy_flow
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location  
* restaurant_search{"location": "Pune"}
  - slot{"location": "Pune"}  
  - action_verify_location
  - slot{"location": "Pune"}  
  - slot{"location_ok": true}
  - utter_ask_cuisine  
* restaurant_search{"cuisine": "Chinese"} 
  - slot{"cuisine": "Chinese"}
  - utter_ask_price_range
* restaurant_search{"price": "Rs. 300 to 700"}   
  - slot{"price": "Rs. 300 to 700"}
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email
* sendmail{"email": "tanyadayanand@gmail.com"}   
  - slot{"email": "tanyadayanand@gmail.com"}
  - action_send__mail
  - slot{"email": "tanyadayanand@gmail.com"}
* thank
  - utter_goodbye
  - action_restart

## story_06_location_out_of_scope_deny
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* out_of_scope
  - action_slot_reset
  - reset_slots 
  - utter_default
  - utter_ask_location
* deny
  - utter_deny
  - utter_goodbye
  - action_restart


<!-- greet, location + cuisine-->
## story_07_location_cuisine_budget_valid_with_email
* greet
  - utter_greet
* restaurant_search{"location": "Mumbai", "cuisine": "chinese"}
  - slot{"location": "Mumbai"}  
  - action_verify_location
  - slot{"location": "Mumbai"}  
  - slot{"location_ok": true}  
  - slot{"cuisine": "chinese"}
  - utter_ask_price_range
* restaurant_search{"price": "More than 700"}   
  - slot{"price": "More than 700"} 
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email
* sendmail{"email": "tanyadayanand@gmail.com"}   
  - slot{"email": "tanyadayanand@gmail.com"}
  - action_send__mail
  - slot{"email": "tanyadayanand@gmail.com"}
* thank
  - utter_goodbye
  - action_restart

## story_08_location_cuisine_budget_valid_no_email
* greet
  - utter_greet
* restaurant_search{"location": "agra", "cuisine": "italian"}
  - slot{"location": "agra"}  
  - action_verify_location
  - slot{"location": "agra"}  
  - slot{"location_ok": true}  
  - slot{"cuisine": "italian"}
  - utter_ask_price_range
* restaurant_search{"price": "Rs. 300 to 700"}   
  - slot{"price": "Rs. 300 to 700"}
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email
* deny
  - utter_goodbye
  - action_restart


## story_09_location_cuisine_budget_with_email
* greet
  - utter_greet
* restaurant_search{"location": "Mumbai", "cuisine": "chinese"}
  - slot{"location": "Mumbai"}  
  - action_verify_location
  - slot{"location": "Mumbai"}  
  - slot{"location_ok": true}  
  - slot{"cuisine": "chinese"}
  - utter_ask_price_range
* restaurant_search{"price": "More than 700"}   
  - slot{"price": "More than 700"} 
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email
* sendmail{"email": "tanyadayanand@gmail.com"}   
  - slot{"email": "tanyadayanand@gmail.com"}
  - action_send__mail
  - slot{"email": "tanyadayanand@gmail.com"}
* thank
  - utter_goodbye
  - action_restart

## story_10_location_cuisine_budget_no_email
* greet
  - utter_greet
* restaurant_search{"location": "agra", "cuisine": "italian"}
  - slot{"location": "agra"}  
  - action_verify_location
  - slot{"location": "agra"}  
  - slot{"location_ok": true}  
  - slot{"cuisine": "italian"}
  - utter_ask_price_range
* restaurant_search{"price": "Rs. 300 to 700"}   
  - slot{"price": "Rs. 300 to 700"}
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email  
* deny
  - utter_goodbye
  - action_restart

## story_11_price_deny
* greet
  - utter_greet
* restaurant_search{"location": "agra", "cuisine": "italian"}
  - slot{"location": "agra"}  
  - action_verify_location
  - slot{"location": "agra"}  
  - slot{"location_ok": true}  
  - slot{"cuisine": "italian"}
  - utter_ask_price_range
* deny
  - utter_deny
  - utter_goodbye
  - action_slot_reset

<!-- no greet, location + cuisine -->
## story_12_no_greet_location_cuisine_budget_valid_no_email
* restaurant_search{"cuisine":"North Indian","location":"Mysore"}
  - slot{"location": "Mysore"}  
  - action_verify_location
  - slot{"location": "Mysore"}  
  - slot{"location_ok": true}  
  - slot{"cuisine": "North Indian"}
  - utter_ask_price_range
* restaurant_search{"price": "More than 700"}   
  - slot{"price": "More than 700"} 
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email  
* deny
  - utter_goodbye
  - action_restart


## story_13_no_greet_location_cuisine_budget_valid_with_email
* restaurant_search{"cuisine":"North Indian","location":"Mysore"}
  - slot{"location": "Mysore"}  
  - action_verify_location
  - slot{"location": "Mysore"}  
  - slot{"location_ok": true}  
  - slot{"cuisine": "North Indian"}
  - utter_ask_price_range
* restaurant_search{"price": "More than 700"}   
  - slot{"price": "More than 700"} 
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email
* sendmail{"email": "tanyadayanand@gmail.com"}   
  - slot{"email": "tanyadayanand@gmail.com"}
  - action_send__mail
  - slot{"email": "tanyadayanand@gmail.com"}
* thank
  - utter_goodbye
  - action_restart


## story_14_no_greet_location_cuisine_valid_retry_no_email
* restaurant_search{"cuisine":"North Indian","location":"Mysore"}
  - slot{"location": "Mysore"}  
  - action_verify_location
  - slot{"location": "Mysore"}  
  - slot{"location_ok": true}  
  - slot{"cuisine": "North Indian"}
  - utter_ask_price_range
* restaurant_search{"price": "More than 700"}   
  - slot{"price": "More than 700"} 
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email  
* deny
  - utter_goodbye
  - action_restart

## story_15_no_greet_location_cuisine_deny
* restaurant_search{"cuisine":"North Indian","location":"Mysore"}
  - slot{"location": "Mysore"}  
  - action_verify_location
  - slot{"location": "Mysore"}  
  - slot{"location_ok": true}  
  - slot{"cuisine": "North Indian"}
* deny
  - utter_deny
  - utter_goodbye
  - action_restart

## story_16_no_greet_location_cuisine_invalid_retry_with_email
* restaurant_search{"cuisine":"North Indian","location":"Mysore"}
  - slot{"location": "Mysore"}  
  - action_verify_location
  - slot{"location": "Mysore"}  
  - slot{"location_ok": true}  
  - slot{"cuisine": "North Indian"}
  - utter_ask_price_range
* restaurant_search{"price": "More than 700"}   
  - slot{"price": "More than 700"} 
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email
* sendmail{"email": "tanyadayanand@gmail.com"}   
  - slot{"email": "tanyadayanand@gmail.com"}
  - action_send__mail
  - slot{"email": "tanyadayanand@gmail.com"}
  - utter_goodbye
  - action_restart
  

<!-- queries with cuisine only -->

<!-- start with greet, followed by question -->
## story_17_greet_cuisine_valid_email
* greet
  - utter_greet
* restaurant_search{"cuisine": "North Indian"}
  - slot{"cuisine": "North Indian"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - slot{"location": "Patna"}  
  - action_verify_location
  - slot{"location": "Patna"}  
  - slot{"location_ok": true}
  - utter_ask_price_range
* restaurant_search{"price": "Rs. 300 to 700"}   
  - slot{"price": "Rs. 300 to 700"}
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email
* sendmail{"email": "tanyadayanand@gmail.com"}   
  - slot{"email": "tanyadayanand@gmail.com"}
  - action_send__mail
  - slot{"email": "tanyadayanand@gmail.com"}
* thank
  - utter_goodbye
  - action_restart

## story_18_greet_cuisine_valid_no_email
* greet
  - utter_greet
* restaurant_search{"cuisine": "North Indian"}
  - slot{"cuisine": "North Indian"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - slot{"location": "Patna"}  
  - action_verify_location
  - slot{"location": "Patna"}  
  - slot{"location_ok": true}
  - utter_ask_price_range
* restaurant_search{"price": "Rs. 300 to 700"}   
  - slot{"price": "Rs. 300 to 700"}
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email  
* deny
  - utter_goodbye
  - action_restart


## story_19_greet_cuisine_no_email
* greet
  - utter_greet
* restaurant_search{"cuisine": "North Indian"}
  - slot{"cuisine": "North Indian"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - slot{"location": "Patna"}  
  - action_verify_location
  - slot{"location": "Patna"}  
  - slot{"location_ok": true}
  - utter_ask_price_range
* restaurant_search{"price": "Rs. 300 to 700"}   
  - slot{"price": "Rs. 300 to 700"}
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email 
* deny
  - utter_goodbye
  - action_restart

## story_20_greet_cuisine_email
* greet
  - utter_greet
* restaurant_search{"cuisine": "North Indian"}
  - slot{"cuisine": "North Indian"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - slot{"location": "Patna"}  
  - action_verify_location
  - slot{"location": "Patna"}  
  - slot{"location_ok": true}
  - utter_ask_price_range
* restaurant_search{"price": "Rs. 300 to 700"}   
  - slot{"price": "Rs. 300 to 700"}
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email 
* sendmail{"email": "tanyadayanand@gmail.com"}   
  - slot{"email": "tanyadayanand@gmail.com"}
  - action_send__mail
  - slot{"email": "tanyadayanand@gmail.com"}
* thank
  - utter_goodbye
  - action_restart

## story_21_greet_cuisine_valid_location_invalid_retry_email
* greet
  - utter_greet
* restaurant_search{"cuisine": "North Indian"}
  - slot{"cuisine": "North Indian"}
  - utter_ask_location
* restaurant_search{"location": "Bansur"}
  - slot{"location": "Bansur"}  
  - action_verify_location
  - slot{"location": null}   
  - slot{"location_ok": false}     
  - action_slot_reset    
  - reset_slots    
  - utter_ask_location 
* restaurant_search{"location": "Bangalore"}
  - slot{"location": "Bangalore"}  
  - action_verify_location
  - slot{"location": "Bangalore"}  
  - slot{"location_ok": true}
  - utter_ask_price_range
* restaurant_search{"price": "Rs. 300 to 700"}   
  - slot{"price": "Rs. 300 to 700"}
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email
* sendmail{"email": "tanyadayanand@gmail.com"}   
  - slot{"email": "tanyadayanand@gmail.com"}
  - action_send__mail
  - slot{"email": "tanyadayanand@gmail.com"}
* thank
  - utter_goodbye
  - action_restart

## story_22_greet_cuisine_valid_location_invalid_retry_no_email
* greet
  - utter_greet
* restaurant_search{"cuisine": "North Indian"}
  - slot{"cuisine": "North Indian"}
  - utter_ask_location
* restaurant_search{"location": "Paota"}
  - slot{"location": "Paota"}  
  - action_verify_location
  - slot{"location": null}   
  - slot{"location_ok": false}     
  - action_slot_reset    
  - reset_slots    
  - utter_ask_location 
* restaurant_search{"location": "Bangalore"}
  - slot{"location": "Bangalore"}  
  - action_verify_location
  - slot{"location": "Bangalore"}  
  - slot{"location_ok": true}
  - utter_ask_price_range
* restaurant_search{"price": "Rs. 300 to 700"}   
  - slot{"price": "Rs. 300 to 700"}
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email
* deny
  - utter_goodbye
  - action_restart

<!-- no greet, start with cuisine -->
## story_23_no_greet_cuisine_valid_email
* restaurant_search{"cuisine": "North Indian"}
  - slot{"cuisine": "North Indian"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - slot{"location": "Patna"}  
  - action_verify_location
  - slot{"location": "Patna"}  
  - slot{"location_ok": true}
  - utter_ask_price_range
* restaurant_search{"price": "Rs. 300 to 700"}   
  - slot{"price": "Rs. 300 to 700"}
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email
* sendmail{"email": "tanyadayanand@gmail.com"}   
  - slot{"email": "tanyadayanand@gmail.com"}
  - action_send__mail
  - slot{"email": "tanyadayanand@gmail.com"}
  - utter_goodbye
  - action_restart

## story_24_no_greet_cuisine_valid_no_email
* restaurant_search{"cuisine": "North Indian"}
  - slot{"cuisine": "North Indian"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - slot{"location": "Patna"}  
  - action_verify_location
  - slot{"location": "Patna"}  
  - slot{"location_ok": true}
  - utter_ask_price_range
* restaurant_search{"price": "Rs. 300 to 700"}   
  - slot{"price": "Rs. 300 to 700"}
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email
* deny
  - utter_goodbye
  - action_restart

## story_25_no_greet_cuisine_no_email
* restaurant_search{"cuisine": "North Indian"}
  - slot{"cuisine": "North Indian"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - slot{"location": "Patna"}  
  - action_verify_location
  - slot{"location": "Patna"}  
  - slot{"location_ok": true}
  - utter_ask_price_range
* restaurant_search{"price": "Rs. 300 to 700"}   
  - slot{"price": "Rs. 300 to 700"}
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email
* deny
  - utter_goodbye
  - action_restart

## story_26_no_greet_cuisine_email
* restaurant_search{"cuisine": "North Indian"}
  - slot{"cuisine": "North Indian"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - slot{"location": "Patna"}  
  - action_verify_location
  - slot{"location": "Patna"}  
  - slot{"location_ok": true}
  - utter_ask_price_range
* restaurant_search{"price": "Rs. 300 to 700"}   
  - slot{"price": "Rs. 300 to 700"}
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email
* sendmail{"email": "tanyadayanand@gmail.com"}   
  - slot{"email": "tanyadayanand@gmail.com"}
  - action_send__mail
  - slot{"email": "tanyadayanand@gmail.com"}
  - utter_goodbye
  - action_restart

## story_27_no_greet_cuisine_valid_location_invalid_retry_email
* restaurant_search{"cuisine": "North Indian"}
  - slot{"cuisine": "North Indian"}
  - utter_ask_location
* restaurant_search{"location": "Rohtas"}
  - slot{"location": "Rohtas"}  
  - action_verify_location
  - slot{"location": null}   
  - slot{"location_ok": false}     
  - action_slot_reset    
  - reset_slots    
  - utter_ask_location 
* restaurant_search{"location": "Bangalore"}
  - slot{"location": "Bangalore"}  
  - action_verify_location
  - slot{"location": "Bangalore"}  
  - slot{"location_ok": true}
  - utter_ask_price_range
* restaurant_search{"price": "Rs. 300 to 700"}   
  - slot{"price": "Rs. 300 to 700"}
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email
* sendmail{"email": "tanyadayanand@gmail.com"}   
  - slot{"email": "tanyadayanand@gmail.com"}
  - action_send__mail
  - slot{"email": "tanyadayanand@gmail.com"}
  - utter_goodbye
  - action_restart

## story_28_no_greet_cuisine_valid_location_invalid_retry_no_email
* restaurant_search{"cuisine": "North Indian"}
  - slot{"cuisine": "North Indian"}
  - utter_ask_location
* restaurant_search{"location": "Balia"}
  - slot{"location": "Balia"}  
  - action_verify_location
  - slot{"location": null}   
  - slot{"location_ok": false}     
  - action_slot_reset    
  - reset_slots    
  - utter_ask_location 
* restaurant_search{"location": "Bangalore"}
  - slot{"location": "Bangalore"}  
  - action_verify_location
  - slot{"location": "Bangalore"}  
  - slot{"location_ok": true}
  - utter_ask_price_range
* restaurant_search{"price": "Rs. 300 to 700"}   
  - slot{"price": "Rs. 300 to 700"}
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email
* deny
  - utter_goodbye
  - action_restart

<!-- queries with location only -->

<!-- start with greet, followed by question -->
## story_29_greet_location_valid_email
* greet
  - utter_greet
* restaurant_search{"location": "Patna"}
  - slot{"location": "Patna"}  
  - action_verify_location
  - slot{"location": "Patna"}  
  - slot{"location_ok": true}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
  - slot{"cuisine": "North Indian"}
  - utter_ask_price_range
* restaurant_search{"price": "Rs. 300 to 700"}   
  - slot{"price": "Rs. 300 to 700"}
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email
* sendmail{"email": "tanyadayanand@gmail.com"}   
  - slot{"email": "tanyadayanand@gmail.com"}
  - action_send__mail
  - slot{"email": "tanyadayanand@gmail.com"}
* thank
  - utter_goodbye
  - action_restart

## story_30_greet_location_valid_no_email
* greet
  - utter_greet
* restaurant_search{"location": "Patna"}
  - slot{"location": "Patna"}  
  - action_verify_location
  - slot{"location": "Patna"}  
  - slot{"location_ok": true}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
  - slot{"cuisine": "North Indian"}
  - utter_ask_price_range
* restaurant_search{"price": "Rs. 300 to 700"}   
  - slot{"price": "Rs. 300 to 700"}
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email
* deny
  - utter_goodbye
  - action_restart

## story_31_greet_location_invalid_retry_no_email
* greet
  - utter_greet
* restaurant_search{"location": "samastipur"}
  - slot{"location": "samastipur"}  
  - action_verify_location
  - slot{"location": null}   
  - slot{"location_ok": false}     
  - action_slot_reset    
  - reset_slots    
  - utter_ask_location 
* restaurant_search{"location": "Patna"}
  - slot{"location": "Patna"}  
  - action_verify_location
  - slot{"location": "Patna"}  
  - slot{"location_ok": true}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - slot{"cuisine": "Chinese"}
  - utter_ask_price_range
* restaurant_search{"price": "Rs. 300 to 700"}   
  - slot{"price": "Rs. 300 to 700"}
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email
* deny
  - utter_goodbye
  - action_restart

## story_32_greet_location_invalid_retry_email
* greet
  - utter_greet
* restaurant_search{"location": "Samastipur"}
  - slot{"location": "Samastipur"}  
  - action_verify_location
  - slot{"location": null}   
  - slot{"location_ok": false}     
  - action_slot_reset    
  - reset_slots    
  - utter_ask_location 
* restaurant_search{"location": "Patna"}
  - slot{"location": "Patna"}  
  - action_verify_location
  - slot{"location": "Patna"}  
  - slot{"location_ok": true}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - slot{"cuisine": "Chinese"}
  - utter_ask_price_range
* restaurant_search{"price": "Rs. 300 to 700"}   
  - slot{"price": "Rs. 300 to 700"}
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email
* sendmail{"email": "tanyadayanand@gmail.com"}   
  - slot{"email": "tanyadayanand@gmail.com"}
  - action_send__mail
  - slot{"email": "tanyadayanand@gmail.com"}
  - utter_goodbye
  - action_restart

<!-- no greet, start with location -->
## story_33_no_greet_location_cuisine_budget_valid_email
* restaurant_search{"location": "Patna"}
  - slot{"location": "Patna"}  
  - action_verify_location
  - slot{"location": "Patna"}  
  - slot{"location_ok": true}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
  - slot{"cuisine": "North Indian"}
  - utter_ask_price_range
* restaurant_search{"price": "Rs. 300 to 700"}   
  - slot{"price": "Rs. 300 to 700"}
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email
* sendmail{"email": "tanyadayanand@gmail.com"}   
  - slot{"email": "tanyadayanand@gmail.com"}
  - action_send__mail
  - slot{"email": "tanyadayanand@gmail.com"}
  - utter_goodbye
  - action_restart

## story_34_no_greet_location_cuisine_budget_valid_no_email
* restaurant_search{"location": "Patna"}
  - slot{"location": "Patna"}  
  - action_verify_location
  - slot{"location": "Patna"}  
  - slot{"location_ok": true}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
  - slot{"cuisine": "North Indian"}
  - utter_ask_price_range
* restaurant_search{"price": "Rs. 300 to 700"}   
  - slot{"price": "Rs. 300 to 700"}
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email
* deny
  - utter_goodbye
  - action_restart

## story_35_no_greet_location_invalid_retry_no_email
* restaurant_search{"location": "Hajipur"}
  - slot{"location": "Hajipur"}  
  - action_verify_location
  - slot{"location": null}   
  - slot{"location_ok": false}     
  - action_slot_reset    
  - reset_slots    
  - utter_ask_location 
* restaurant_search{"location": "Patna"}
  - slot{"location": "Patna"}  
  - action_verify_location
  - slot{"location": "Patna"}  
  - slot{"location_ok": true}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - slot{"cuisine": "Chinese"}
  - utter_ask_price_range
* restaurant_search{"price": "Rs. 300 to 700"}   
  - slot{"price": "Rs. 300 to 700"}
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email
* deny
  - utter_goodbye
  - action_restart

## story_36_no_greet_location_invalid_retry_email
* restaurant_search{"location": "Vaishali"}
  - slot{"location": "Vaishali"}  
  - action_verify_location
  - slot{"location": null}   
  - slot{"location_ok": false}     
  - action_slot_reset    
  - reset_slots    
  - utter_ask_location 
* restaurant_search{"location": "Patna"}
  - slot{"location": "Patna"}  
  - action_verify_location
  - slot{"location": "Patna"}  
  - slot{"location_ok": true}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - slot{"cuisine": "Chinese"}
  - utter_ask_price_range
* restaurant_search{"price": "Rs. 300 to 700"}   
  - slot{"price": "Rs. 300 to 700"}
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email
* sendmail{"email": "tanyadayanand@gmail.com"}   
  - slot{"email": "tanyadayanand@gmail.com"}
  - action_send__mail
  - slot{"email": "tanyadayanand@gmail.com"}
* thank
  - utter_goodbye
  - action_restart

<!-- cuisine + location, both invalid -->

<!-- greet, followed by question -->
## story_37_greet_cuisine_and_location_invalid_retry_email
* greet
  - utter_greet
* restaurant_search{"location": "Sarnath", "cuisine": "french"}
  - slot{"location": "Sarnath"}  
  - action_verify_location
  - slot{"location": null}   
  - slot{"location_ok": false}     
  - action_slot_reset    
  - reset_slots    
  - utter_ask_location
* restaurant_search{"location": "Delhi"}
  - slot{"location": "Delhi"}  
  - action_verify_location
  - slot{"location": "Delhi"}  
  - slot{"location_ok": true}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - slot{"cuisine": "Chinese"}
  - utter_ask_price_range
* restaurant_search{"price": "Rs. 300 to 700"}   
  - slot{"price": "Rs. 300 to 700"}
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email
* sendmail{"email": "tanyadayanand@gmail.com"}   
  - slot{"email": "tanyadayanand@gmail.com"}
  - action_send__mail
  - slot{"email": "tanyadayanand@gmail.com"}
  - utter_goodbye
  - action_restart

## story_38_greet_cuisine_and_location_invalid_retry_no_email
* greet
  - utter_greet
* restaurant_search{"location": "Conncticut", "cuisine": "asian"}
  - slot{"location": "Conncticut"}  
  - action_verify_location
  - slot{"location": null}   
  - slot{"location_ok": false}     
  - action_slot_reset    
  - reset_slots    
  - utter_ask_location 
* restaurant_search{"location": "Bangalore"}
  - slot{"location": "Bangalore"}  
  - action_verify_location
  - slot{"location": "Bangalore"}  
  - slot{"location_ok": true}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
  - slot{"cuisine": "italian"}
  - utter_ask_price_range
* restaurant_search{"price": "Rs. 300 to 700"}   
  - slot{"price": "Rs. 300 to 700"}
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email
* deny
  - utter_goodbye
  - action_restart

<!-- no greet -->
## story_39_no_greet_cuisine_and_location_invalid_retry_email
* restaurant_search{"location": "Kharadi", "cuisine": "french"}
  - slot{"location": "Kharadi"}  
  - action_verify_location
  - slot{"location": null}   
  - slot{"location_ok": false}     
  - action_slot_reset    
  - reset_slots    
  - utter_ask_location 
* restaurant_search{"location": "Chennai"}
  - slot{"location": "Chennai"}  
  - action_verify_location
  - slot{"location": "Chennai"}  
  - slot{"location_ok": true}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
  - slot{"cuisine": "American"}
  - utter_ask_price_range
* restaurant_search{"price": "Rs. 300 to 700"}   
  - slot{"price": "Rs. 300 to 700"}
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email
* sendmail{"email": "tanyadayanand@gmail.com"}   
  - slot{"email": "tanyadayanand@gmail.com"}
  - action_send__mail
  - slot{"email": "tanyadayanand@gmail.com"}
  - utter_goodbye
  - action_restart

## story_40_no_greet_cuisine_and_location_invalid_retry_no_email
* restaurant_search{"location": "Hinjewadi", "cuisine": "Roman"}
  - slot{"location": "Hinjewadi"}  
  - action_verify_location
  - slot{"location": null}   
  - slot{"location_ok": false}    
  - action_slot_reset    
  - reset_slots    
  - utter_ask_location 
* restaurant_search{"location": "Vizag"}
  - slot{"location": "Vizag"}  
  - action_verify_location
  - slot{"location": "Vizag"}  
  - slot{"location_ok": true}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
  - slot{"cuisine": "italian"}
  - utter_ask_price_range
* restaurant_search{"price": "Rs. 300 to 700"}   
  - slot{"price": "Rs. 300 to 700"}
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
* deny
  - utter_goodbye
  - action_restart

<!-- invalid search such as no restaurant are found-->
## story_41_location_cuisine_valid_search_invalid
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "Bangalore"}
  - slot{"location": "Bangalore"}  
  - action_verify_location
  - slot{"location": "Bangalore"}  
  - slot{"location_ok": true}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - slot{"cuisine": "Chinese"}
  - utter_ask_price_range
* restaurant_search{"price": "Lesser than Rs. 300"}   
  - slot{"price": "Lesser than Rs. 300"}
  - action_search_restaurants
  - slot{"search_validity" : "invalid"}
  - utter_search_invalid
  - utter_goodbye
  - action_restart

## story_42_location_invalid_retry_search_invalid
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "Chomu"}
  - slot{"location": "Chomu"}  
  - action_verify_location
  - slot{"location": null}   
  - slot{"location_ok": false}     
  - action_slot_reset    
  - reset_slots    
  - utter_ask_location 
* restaurant_search{"location": "Bangalore"}
  - slot{"location": "Bangalore"}  
  - action_verify_location
  - slot{"location": "Bangalore"}  
  - slot{"location_ok": true}
  - utter_ask_cuisine  
* restaurant_search{"cuisine": "Chinese"}
  - slot{"cuisine": "Chinese"}
  - utter_ask_price_range
* restaurant_search{"price": "Lesser than Rs. 300"}   
  - slot{"price": "Lesser than Rs. 300"}
  - action_search_restaurants
  - slot{"search_validity" : "invalid"}
  - utter_search_invalid
  - utter_goodbye
  - action_restart

## story_43_location_cuisine_budget_valid_search_invalid
* greet
  - utter_greet
* restaurant_search{"location": "Mumbai", "cuisine": "chinese"}
  - slot{"location": "Mumbai"}  
  - action_verify_location
  - slot{"location": "Mumbai"}  
  - slot{"location_ok": true}  
  - slot{"cuisine": "chinese"}
  - utter_ask_price_range
* restaurant_search{"price": "More than 700"}   
  - slot{"price": "More than 700"} 
  - action_search_restaurants
  - slot{"search_validity" : "invalid"}
  - utter_search_invalid
  - utter_goodbye
  - action_restart
  
## story_44_location_cuisine_search_invalid
* greet
  - utter_greet
* restaurant_search{"location": "Mumbai", "cuisine": "chinese"}
  - slot{"location": "Mumbai"}  
  - action_verify_location
  - slot{"location": "Mumbai"}  
  - slot{"location_ok": true}  
  - slot{"cuisine": "chinese"}
  - utter_ask_price_range
* restaurant_search{"price": "More than 700"}   
  - slot{"price": "More than 700"} 
  - action_search_restaurants
  - slot{"search_validity" : "invalid"}
  - utter_search_invalid
  - utter_goodbye
  - action_restart

## story_45_no_greet_location_cuisine_budget_valid_search_invalid
* restaurant_search{"cuisine":"North Indian","location":"Mysore"}
  - slot{"location": "Mysore"}  
  - action_verify_location
  - slot{"location": "Mysore"}  
  - slot{"location_ok": true}  
  - slot{"cuisine": "North Indian"}
  - utter_ask_price_range
* restaurant_search{"price": "More than 700"}   
  - slot{"price": "More than 700"} 
  - action_search_restaurants
  - slot{"search_validity" : "invalid"}
  - utter_search_invalid
  - utter_goodbye
  - action_restart

## story_46_no_greet_location_cuisine_invalid_retry_search_invalid
* restaurant_search{"cuisine":"North Indian","location":"Mysore"}
  - slot{"location": "Mysore"}  
  - action_verify_location
  - slot{"location": "Mysore"}  
  - slot{"location_ok": true}  
  - slot{"cuisine": "North Indian"}
  - utter_ask_price_range
* restaurant_search{"price": "More than 700"}   
  - slot{"price": "More than 700"} 
  - action_search_restaurants
  - slot{"search_validity" : "invalid"}
  - utter_search_invalid
  - utter_goodbye
  - action_restart
  
## story_47_greet_cuisine_valid_search_invalid
* greet
  - utter_greet
* restaurant_search{"cuisine": "North Indian"}
  - slot{"cuisine": "North Indian"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - slot{"location": "Patna"}  
  - action_verify_location
  - slot{"location": "Patna"}  
  - slot{"location_ok": true}
  - utter_ask_price_range
* restaurant_search{"price": "Rs. 300 to 700"}   
  - slot{"price": "Rs. 300 to 700"}
  - action_search_restaurants
  - slot{"search_validity" : "invalid"}
  - utter_search_invalid
  - utter_goodbye
  - action_restart

## story_48_greet_cuisine_invalid_retry_search_invalid
* greet
  - utter_greet
* restaurant_search{"cuisine": "North Indian"}
  - slot{"cuisine": "North Indian"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - slot{"location": "Patna"}  
  - action_verify_location
  - slot{"location": "Patna"}  
  - slot{"location_ok": true}
  - utter_ask_price_range
* restaurant_search{"price": "Rs. 300 to 700"}   
  - slot{"price": "Rs. 300 to 700"}
  - action_search_restaurants
  - slot{"search_validity" : "invalid"}
  - utter_search_invalid
  - utter_goodbye
  - action_restart

## story_49_greet_cuisine_valid_location_invalid_retry_search_invalid
* greet
  - utter_greet
* restaurant_search{"cuisine": "North Indian"}
  - slot{"cuisine": "North Indian"}
  - utter_ask_location
* restaurant_search{"location": "Chomu"}
  - slot{"location": "Chomu"}  
  - action_verify_location
  - slot{"location": null}   
  - slot{"location_ok": false}     
  - action_slot_reset    
  - reset_slots    
  - utter_ask_location 
* restaurant_search{"location": "Bangalore"}
  - slot{"location": "Bangalore"}  
  - action_verify_location
  - slot{"location": "Bangalore"}  
  - slot{"location_ok": true}
  - utter_ask_price_range
* restaurant_search{"price": "Rs. 300 to 700"}   
  - slot{"price": "Rs. 300 to 700"}
  - action_search_restaurants
  - slot{"search_validity" : "invalid"}
  - utter_search_invalid
  - utter_goodbye
  - action_restart
  
## story_50_no_greet_cuisine_valid_search_invalid
* restaurant_search{"cuisine": "North Indian"}
  - slot{"cuisine": "North Indian"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - slot{"location": "Patna"}  
  - action_verify_location
  - slot{"location": "Patna"}  
  - slot{"location_ok": true}
  - utter_ask_price_range
* restaurant_search{"price": "Rs. 300 to 700"}   
  - slot{"price": "Rs. 300 to 700"}
  - action_search_restaurants
  - slot{"search_validity" : "invalid"}
  - utter_search_invalid
  - utter_goodbye
  - action_restart

## story_51_no_greet_cuisine_search_invalid
* restaurant_search{"cuisine": "North Indian"}
  - slot{"cuisine": "North Indian"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - slot{"location": "Patna"}  
  - action_verify_location
  - slot{"location": "Patna"}  
  - slot{"location_ok": true}
  - utter_ask_price_range
* restaurant_search{"price": "Rs. 300 to 700"}   
  - slot{"price": "Rs. 300 to 700"}
  - action_search_restaurants
  - slot{"search_validity" : "invalid"}
  - utter_search_invalid
  - utter_goodbye
  - action_restart

## story_52_no_greet_cuisine_valid_location_invalid_retry_search_invalid
* restaurant_search{"cuisine": "North Indian"}
  - slot{"cuisine": "North Indian"}
  - utter_ask_location
* restaurant_search{"location": "Balia"}
  - slot{"location": "Balia"}  
  - action_verify_location
  - slot{"location": null}   
  - slot{"location_ok": false}     
  - action_slot_reset    
  - reset_slots    
  - utter_ask_location 
* restaurant_search{"location": "Bangalore"}
  - slot{"location": "Bangalore"}  
  - action_verify_location
  - slot{"location": "Bangalore"}  
  - slot{"location_ok": true}
  - utter_ask_price_range
* restaurant_search{"price": "Rs. 300 to 700"}   
  - slot{"price": "Rs. 300 to 700"}
  - action_search_restaurants
  - slot{"search_validity" : "invalid"}
  - utter_search_invalid
  - utter_goodbye
  - action_restart

## story_53_greet_location_valid_search_invalid
* greet
  - utter_greet
* restaurant_search{"location": "Patna"}
  - slot{"location": "Patna"}  
  - action_verify_location
  - slot{"location": "Patna"}  
  - slot{"location_ok": true}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
  - slot{"cuisine": "North Indian"}
  - utter_ask_price_range
* restaurant_search{"price": "Rs. 300 to 700"}   
  - slot{"price": "Rs. 300 to 700"}
  - action_search_restaurants
  - slot{"search_validity" : "invalid"}
  - utter_search_invalid
  - utter_goodbye
  - action_restart

## story_54_greet_location_invalid_retry_no_email
* greet
  - utter_greet
* restaurant_search{"location": "Jobner"}
  - slot{"location": "Jobner"}  
  - action_verify_location
  - slot{"location": null}   
  - slot{"location_ok": false}     
  - action_slot_reset    
  - reset_slots    
  - utter_ask_location 
* restaurant_search{"location": "Patna"}
  - slot{"location": "Patna"}  
  - action_verify_location
  - slot{"location": "Patna"}  
  - slot{"location_ok": true}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - slot{"cuisine": "Chinese"}
  - utter_ask_price_range
* restaurant_search{"price": "Rs. 300 to 700"}   
  - slot{"price": "Rs. 300 to 700"}
  - action_search_restaurants
  - slot{"search_validity" : "invalid"}
  - utter_search_invalid
  - utter_goodbye
  - action_restart

## story_55_no_greet_location_cuisine_budget_valid_search_invalid
* restaurant_search{"location": "Patna"}
  - slot{"location": "Patna"}  
  - action_verify_location
  - slot{"location": "Patna"}  
  - slot{"location_ok": true}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
  - slot{"cuisine": "North Indian"}
  - utter_ask_price_range
* restaurant_search{"price": "Rs. 300 to 700"}   
  - slot{"price": "Rs. 300 to 700"}
  - action_search_restaurants
  - slot{"search_validity" : "invalid"}
  - utter_search_invalid
  - utter_goodbye
  - action_restart

## story_56_no_greet_location_invalid_retry_search_invalid
* restaurant_search{"location": "Darbhanga"}
  - slot{"location": "Darbhanga"}  
  - action_verify_location
  - slot{"location": null}   
  - slot{"location_ok": false}     
  - action_slot_reset    
  - reset_slots    
  - utter_ask_location 
* restaurant_search{"location": "Goa"}
  - slot{"location": "Goa"}  
  - action_verify_location
  - slot{"location": "Goa"}  
  - slot{"location_ok": true}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - slot{"cuisine": "Chinese"}
  - utter_ask_price_range
* restaurant_search{"price": "Rs. 300 to 700"}   
  - slot{"price": "Rs. 300 to 700"}
  - action_search_restaurants
  - slot{"search_validity" : "invalid"}
  - utter_search_invalid
  - utter_goodbye
  - action_restart

## story_57_greet_cuisine_and_location_invalid_retry_search_invalid
* greet
  - utter_greet
* restaurant_search{"location": "Dehu", "cuisine": "french"}
  - slot{"location": "Dehu"}  
  - action_verify_location
  - slot{"location": null}   
  - slot{"location_ok": false}     
  - action_slot_reset    
  - reset_slots    
  - utter_ask_location 
* restaurant_search{"location": "Delhi"}
  - slot{"location": "Delhi"}  
  - action_verify_location
  - slot{"location": "Delhi"}  
  - slot{"location_ok": true}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "french"}
  - slot{"cuisine": "french"}
  - utter_ask_price_range
* restaurant_search{"price": "Rs. 300 to 700"}   
  - slot{"price": "Rs. 300 to 700"}
  - action_search_restaurants
  - slot{"search_validity" : "invalid"}
  - utter_search_invalid
  - utter_goodbye
  - action_restart

## story_58_no_greet_cuisine_and_location_invalid_retry_search_invalid
* restaurant_search{"location": "Mahabaleswar", "cuisine": "french"}
  - slot{"location": "Mahabaleswar"}  
  - action_verify_location
  - slot{"location": null}   
  - slot{"location_ok": false}     
  - action_slot_reset    
  - reset_slots    
  - utter_ask_location 
* restaurant_search{"location": "Delhi"}
  - slot{"location": "Delhi"}  
  - action_verify_location
  - slot{"location": "Delhi"}  
  - slot{"location_ok": true}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
  - slot{"cuisine": "south indian"}
  - utter_ask_price_range
* restaurant_search{"price": "Rs. 300 to 700"}   
  - slot{"price": "Rs. 300 to 700"}
  - action_search_restaurants
  - slot{"search_validity" : "invalid"}
  - utter_search_invalid
  - utter_goodbye
  - action_restart
  
<!-- stop conversation with denial-->
## story_59_location_invalid_retry
* restaurant_search{"location":"Jamui", "cuisine":"mexican"}
  - slot{"location": "Jamui"}  
  - action_verify_location
  - slot{"location": null}   
  - slot{"location_ok": false}
  - slot{"cuisine": "mexican"}  
  - action_slot_reset    
  - reset_slots    
  - utter_ask_location 
* deny
  - utter_deny
  - utter_goodbye
  - action_restart

## story_60_location_valid_cuisine_valid
* restaurant_search{"location":"Kolkata", "cuisine":"mexican"}
  - slot{"location": "Kolkata"}  
  - action_verify_location
  - slot{"location": "Kolkata"}  
  - slot{"location_ok": true}
  - slot{"cuisine": "mexican"}
  - utter_ask_price_range
* deny
  - utter_deny
  - utter_goodbye
  - action_restart

## story_61_no_greet_location_invalid_retry
* restaurant_search{"location": "Jodhpur"}
  - slot{"location": "Jodhpur"}  
  - action_verify_location
  - slot{"location": null}   
  - slot{"location_ok": false}     
  - action_slot_reset    
  - reset_slots    
  - utter_ask_location 
* deny
  - utter_deny
  - utter_goodbye
  - action_restart

## story_62_greet_location_invalid_retry
* greet
  - utter_greet
* restaurant_search{"location": "Jodhpur"}
  - slot{"location": "Jodhpur"}  
  - action_verify_location
  - slot{"location": null}   
  - slot{"location_ok": false}     
  - action_slot_reset    
  - reset_slots    
  - utter_ask_location 
* deny
  - utter_deny
  - utter_goodbye
  - action_restart

## story_63_no_greet_cuisine_invalid_retry
* restaurant_search{"cuisine": "Japanese"}
 - utter_ask_cuisine
* deny
  - utter_deny
  - utter_goodbye
  - action_restart

## story_64_greet_cuisine_invalid_retry
* greet
  - utter_greet
* restaurant_search{"cuisine": "Japanese"}
  - utter_ask_cuisine
* deny
  - utter_deny
  - utter_goodbye
  - action_restart

<!-- drop out of conversation with goodbye-->
## story_65_greet_drop
* greet
  - utter_greet
* goodbye
  - utter_goodbye
  - action_restart

## story_66_restaurant_search_drop
* restaurant_search
  - utter_ask_location
* goodbye
  - utter_goodbye
  - action_restart

## story_67_no_greet_location_invalid_drop
* restaurant_search{"location": "Lonawala"}
  - slot{"location": "Lonawala"}  
  - action_verify_location
  - slot{"location": null}   
  - slot{"location_ok": false}     
  - action_slot_reset    
  - reset_slots    
  - utter_ask_location 
* goodbye
  - utter_goodbye
  - action_restart

## story_68_no_greet_location_invalid_retry_cuisine_drop
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "Lonawala"}
  - slot{"location": "Lonawala"}  
  - action_verify_location
  - slot{"location": null}   
  - slot{"location_ok": false}     
  - action_slot_reset    
  - reset_slots    
  - utter_ask_location 
* restaurant_search{"location": "Bangalore"}
  - slot{"location": "Bangalore"}  
  - action_verify_location
  - slot{"location": "Bangalore"}  
  - slot{"location_ok": true}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - slot{"cuisine": "Chinese"} 
  - utter_ask_price_range
* restaurant_search{"price": "Rs. 300 to 700"}   
  - slot{"price": "Rs. 300 to 700"}
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
* goodbye
  - utter_goodbye
  - action_restart

## story_69_no_greet_location_invalid_retry_cuisine_drop
* restaurant_search{"location": "Lonawala"}
  - slot{"location": "Lonawala"}  
  - action_verify_location
  - slot{"location": null}   
  - slot{"location_ok": false}     
  - action_slot_reset    
  - reset_slots    
  - utter_ask_location 
* restaurant_search{"location": "Bangalore"}
  - slot{"location": "Bangalore"}  
  - action_verify_location
  - slot{"location": "Bangalore"}  
  - slot{"location_ok": true}
  - utter_ask_cuisine
* goodbye
  - utter_goodbye
  - action_restart

## story_70_no_greet_location_invalid_retry_drop
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "Lonawala"}
  - slot{"location": "Lonawala"}  
  - action_verify_location
  - slot{"location": null}   
  - slot{"location_ok": false}     
  - action_slot_reset    
  - reset_slots    
  - utter_ask_location 
* goodbye
  - utter_goodbye
  - action_restart

## story_71_ask_location_drop
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* goodbye
  - utter_goodbye
  - action_restart

## story_72_no_greet_location_invalid_retry_email_drop
* restaurant_search{"location": "Lonawala"}
  - slot{"location": "Lonawala"}  
  - action_verify_location
  - slot{"location": null}   
  - slot{"location_ok": false}     
  - action_slot_reset    
  - reset_slots    
  - utter_ask_location 
* restaurant_search{"location": "Bangalore"}
  - slot{"location": "Bangalore"}  
  - action_verify_location
  - slot{"location": "Bangalore"}  
  - slot{"location_ok": true}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - slot{"cuisine": "Chinese"}
  - utter_ask_price_range
* restaurant_search{"price": "Rs. 300 to 700"}   
  - slot{"price": "Rs. 300 to 700"}
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
* goodbye
  - utter_goodbye
  - action_restart

## story_73_no_greet_location_invalid_retry_email_drop
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "Lonawala"}
  - slot{"location": "Lonawala"}  
  - action_verify_location
  - slot{"location": null}   
  - slot{"location_ok": false}     
  - action_slot_reset    
  - reset_slots    
  - utter_ask_location 
* restaurant_search{"location": "Bangalore"}
  - slot{"location": "Bangalore"}  
  - action_verify_location
  - slot{"location": "Bangalore"}  
  - slot{"location_ok": true}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - slot{"cuisine": "Chinese"}
  - utter_ask_price_range
* restaurant_search{"price": "Rs. 300 to 700"}   
  - slot{"price": "Rs. 300 to 700"}
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
* goodbye
  - utter_goodbye
  - action_restart

<!-- handling out of scope responses -->
## story_74_greet_out_of_scope
* greet
  - utter_greet
* out_of_scope
  - utter_default
  - utter_goodbye
  - action_restart

## story_75_no_greet_location_retry_out_of_scope
* restaurant_search
  - utter_ask_location
* out_of_scope
  - action_slot_reset
  - reset_slots 
  - utter_default
  - utter_ask_location
* out_of_scope
  - utter_goodbye
  - action_restart

## story_76_no_greet_location_invalid_out_of_scope
* restaurant_search{"location": "New York"}
  - slot{"location": "New York"}  
  - action_verify_location
  - slot{"location": null}   
  - slot{"location_ok": false}     
  - action_slot_reset    
  - reset_slots    
  - utter_ask_location 
* out_of_scope
  - utter_goodbye
  - action_restart
  
<!-- queries with price only -->  
  
<!-- greet, location + cuisine-->  
## story_77_location_cuisine_valid_with_email
* greet
  - utter_greet
* restaurant_search{"price": "Lesser than Rs. 300"}   
  - slot{"price": "Lesser than Rs. 300"}
  - utter_ask_location
* restaurant_search{"location": "Bangalore"}
  - slot{"location": "Bangalore"}  
  - action_verify_location
  - slot{"location": "Bangalore"}  
  - slot{"location_ok": true}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - slot{"cuisine": "Chinese"}
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email
* sendmail{"email": "tanyadayanand@gmail.com"}   
  - slot{"email": "tanyadayanand@gmail.com"}
  - action_send__mail
  - slot{"email": "tanyadayanand@gmail.com"}
* thank
  - utter_goodbye
  - action_restart
  
## story_78_location_invalid_retry_with_email
* greet
  - utter_greet
* restaurant_search{"price": "Lesser than Rs. 300"}   
  - slot{"price": "Lesser than Rs. 300"}
  - utter_ask_location
* restaurant_search{"location": "Manorpur"}
  - slot{"location": "Manorpur"}  
  - action_verify_location
  - slot{"location": null}   
  - slot{"location_ok": false}     
  - action_slot_reset    
  - reset_slots    
  - utter_ask_location 
* restaurant_search{"location": "Bangalore"}
  - slot{"location": "Bangalore"}  
  - action_verify_location
  - slot{"location": "Bangalore"}  
  - slot{"location_ok": true}
  - utter_ask_cuisine  
* restaurant_search{"cuisine": "Chinese"}
  - slot{"cuisine": "Chinese"}
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email
* sendmail{"email": "tanyadayanand@gmail.com"}   
  - slot{"email": "tanyadayanand@gmail.com"}
  - action_send__mail
  - slot{"email": "tanyadayanand@gmail.com"}
* thank
  - utter_goodbye
  - action_restart
  
## story_79_location_cuisine_valid_no_email
* greet
  - utter_greet
* restaurant_search{"price": "Lesser than Rs. 300"}   
  - slot{"price": "Lesser than Rs. 300"}
  - utter_ask_location
* restaurant_search{"location": "Bangalore"}
  - slot{"location": "Bangalore"}  
  - action_verify_location
  - slot{"location": "Bangalore"}  
  - slot{"location_ok": true}  
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - slot{"cuisine": "Chinese"}
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email 
* deny
  - utter_goodbye
  - action_restart
  
## story_80_location_cuisine_budget_valid_with_email
* greet
  - utter_greet
* restaurant_search{"location": "Mumbai", "price": "More than 700"}
  - slot{"location": "Mumbai"}  
  - action_verify_location
  - slot{"location": "Mumbai"}  
  - slot{"location_ok": true}  
  - slot{"price": "More than 700"} 
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - slot{"cuisine": "Chinese"}
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email
* sendmail{"email": "tanyadayanand@gmail.com"}   
  - slot{"email": "tanyadayanand@gmail.com"}
  - action_send__mail
  - slot{"email": "tanyadayanand@gmail.com"}
* thank
  - utter_goodbye
  - action_restart

<!-- no greet, location + cuisine -->
## story_81_no_greet_location_cuisine_budget_valid_no_email
* restaurant_search{"cuisine":"North Indian","price": "More than 700"}
  - slot{"price": "More than 700"} 
  - slot{"cuisine": "North Indian"}
  - utter_ask_location
* restaurant_search{"location": "Bangalore"}
  - slot{"location": "Bangalore"}  
  - action_verify_location
  - slot{"location": "Bangalore"}  
  - slot{"location_ok": true}  
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email  
* deny
  - utter_goodbye
  - action_restart


## story_82_no_greet_location_cuisine_budget_valid_with_email
* restaurant_search{"cuisine":"North Indian","price": "More than 700"}
  - slot{"price": "More than 700"} 
  - slot{"cuisine": "North Indian"}
  - utter_ask_location
* restaurant_search{"location": "Bangalore"}
  - slot{"location": "Bangalore"}  
  - action_verify_location
  - slot{"location": "Bangalore"}  
  - slot{"location_ok": true} 
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email
* sendmail{"email": "tanyadayanand@gmail.com"}   
  - slot{"email": "tanyadayanand@gmail.com"}
  - action_send__mail
  - slot{"email": "tanyadayanand@gmail.com"}
* thank
  - utter_goodbye
  - action_restart


## story_83_no_greet_location_cuisine_valid_retry_no_email
* restaurant_search{"location": "Mumbai", "price": "More than 700"}
  - slot{"location": "Mumbai"}  
  - action_verify_location
  - slot{"location": "Mumbai"}  
  - slot{"location_ok": true}  
  - slot{"price": "More than 700"} 
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - slot{"cuisine": "Chinese"}
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email
* deny
  - utter_goodbye
  - action_restart

## story_84_no_greet_location_cuisine_deny
* restaurant_search{"price": "More than 700", "location":"Mysore"}
  - slot{"location": "Mysore"}  
  - action_verify_location
  - slot{"location": "Mysore"}  
  - slot{"location_ok": true}  
  - slot{"price": "More than 700"} 
* deny
  - utter_deny
  - utter_goodbye
  - action_restart
  
<!-- no greet, location + cuisine + price-->

## story_85_no_greet_location_cuisine_price_with_email
* restaurant_search{"cuisine":"North Indian", "location":"Mysore", "price": "More than 700"}
  - slot{"location": "Mysore"}  
  - action_verify_location
  - slot{"location": "Mysore"}  
  - slot{"location_ok": true}  
  - slot{"cuisine": "North Indian"}
  - slot{"price": "More than 700"} 
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email
* sendmail{"email": "tanyadayanand@gmail.com"}   
  - slot{"email": "tanyadayanand@gmail.com"}
  - action_send__mail
  - slot{"email": "tanyadayanand@gmail.com"}
  - utter_goodbye
  - action_restart
  
## story_86_greet_location_cuisine_price_with_email
* greet
  - utter_greet
* restaurant_search{"cuisine":"North Indian", "location":"Mysore", "price": "More than 700"}
  - slot{"location": "Mysore"}  
  - action_verify_location
  - slot{"location": "Mysore"}  
  - slot{"location_ok": true}  
  - slot{"cuisine": "North Indian"}
  - slot{"price": "More than 700"} 
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email
* sendmail{"email": "tanyadayanand@gmail.com"}   
  - slot{"email": "tanyadayanand@gmail.com"}
  - action_send__mail
  - slot{"email": "tanyadayanand@gmail.com"}
  - utter_goodbye
  - action_restart

## story_87_no_greet_location_cuisine_budget_valid_no_email
* greet
  - utter_greet
* restaurant_search{"cuisine":"North Indian", "location":"Mysore", "price": "More than 700"}
  - slot{"location": "Mysore"}  
  - action_verify_location
  - slot{"location": "Mysore"}  
  - slot{"location_ok": true}  
  - slot{"cuisine": "North Indian"}
  - slot{"price": "More than 700"} 
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email  
* deny
  - utter_goodbye
  - action_restart  

<!-- queries with price only with no restaurant found-->  
  
<!-- greet, location + cuisine-->  
## story_88_location_cuisine_valid_with_email
* greet
  - utter_greet
* restaurant_search{"price": "Lesser than Rs. 300"}   
  - slot{"price": "Lesser than Rs. 300"}
  - utter_ask_location
* restaurant_search{"location": "Bangalore"}
  - slot{"location": "Bangalore"}  
  - action_verify_location
  - slot{"location": "Bangalore"}  
  - slot{"location_ok": true}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - slot{"cuisine": "Chinese"}
  - action_search_restaurants
  - slot{"search_validity" : "invalid"}
  - utter_search_invalid
  - utter_goodbye
  - action_restart
  
## story_89_location_invalid_retry_with_email
* greet
  - utter_greet
* restaurant_search{"price": "Lesser than Rs. 300"}   
  - slot{"price": "Lesser than Rs. 300"}
  - utter_ask_location
* restaurant_search{"location": "Manorpur"}
  - slot{"location": "Manorpur"}  
  - action_verify_location
  - slot{"location": null}   
  - slot{"location_ok": false}     
  - action_slot_reset    
  - reset_slots    
  - utter_ask_location 
* restaurant_search{"location": "Bangalore"}
  - slot{"location": "Bangalore"}  
  - action_verify_location
  - slot{"location": "Bangalore"}  
  - slot{"location_ok": true}
  - utter_ask_cuisine  
* restaurant_search{"cuisine": "Chinese"}
  - slot{"cuisine": "Chinese"}
  - action_search_restaurants
  - slot{"search_validity" : "invalid"}
  - utter_search_invalid
  - utter_goodbye
  - action_restart
  
## story_90_location_cuisine_valid_no_email
* greet
  - utter_greet
* restaurant_search{"price": "Lesser than Rs. 300"}   
  - slot{"price": "Lesser than Rs. 300"}
  - utter_ask_location
* restaurant_search{"location": "Bangalore"}
  - slot{"location": "Bangalore"}  
  - action_verify_location
  - slot{"location": "Bangalore"}  
  - slot{"location_ok": true}  
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - slot{"cuisine": "Chinese"}
  - action_search_restaurants
  - slot{"search_validity" : "invalid"}
  - utter_search_invalid
  - utter_goodbye
  - action_restart
  
## story_91_location_cuisine_budget_valid_with_email
* greet
  - utter_greet
* restaurant_search{"location": "Mumbai", "price": "More than 700"}
  - slot{"location": "Mumbai"}  
  - action_verify_location
  - slot{"location": "Mumbai"}  
  - slot{"location_ok": true}  
  - slot{"price": "More than 700"} 
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - slot{"cuisine": "Chinese"}
  - action_search_restaurants
  - slot{"search_validity" : "invalid"}
  - utter_search_invalid
  - utter_goodbye
  - action_restart

<!-- no greet, location + cuisine -->
## story_92_no_greet_location_cuisine_budget_valid_no_email
* restaurant_search{"cuisine":"North Indian","price": "More than 700"}
  - slot{"price": "More than 700"} 
  - slot{"cuisine": "North Indian"}
  - utter_ask_location
* restaurant_search{"location": "Bangalore"}
  - slot{"location": "Bangalore"}  
  - action_verify_location
  - slot{"location": "Bangalore"}  
  - slot{"location_ok": true}  
  - action_search_restaurants
  - slot{"search_validity" : "invalid"}
  - utter_search_invalid
  - utter_goodbye
  - action_restart


## story_93_no_greet_location_cuisine_budget_valid_with_email
* restaurant_search{"cuisine":"North Indian","price": "More than 700"}
  - slot{"price": "More than 700"} 
  - slot{"cuisine": "North Indian"}
  - utter_ask_location
* restaurant_search{"location": "Bangalore"}
  - slot{"location": "Bangalore"}  
  - action_verify_location
  - slot{"location": "Bangalore"}  
  - slot{"location_ok": true} 
  - action_search_restaurants
  - slot{"search_validity" : "invalid"}
  - utter_search_invalid
  - utter_goodbye
  - action_restart


## story_94_no_greet_location_cuisine_valid_retry_no_email
* restaurant_search{"location": "Mumbai", "price": "More than 700"}
  - slot{"location": "Mumbai"}  
  - action_verify_location
  - slot{"location": "Mumbai"}  
  - slot{"location_ok": true}  
  - slot{"price": "More than 700"} 
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - slot{"cuisine": "Chinese"}
  - action_search_restaurants
  - slot{"search_validity" : "invalid"}
  - utter_search_invalid
  - utter_goodbye
  - action_restart

## story_95_no_greet_location_cuisine_deny
* restaurant_search{"price": "More than 700", "location":"Mysore"}
  - slot{"location": "Mysore"}  
  - action_verify_location
  - slot{"location": "Mysore"}  
  - slot{"location_ok": true}  
  - slot{"price": "More than 700"} 
* deny
  - utter_deny
  - utter_goodbye
  - action_restart
  
<!-- no greet, location + cuisine + price-->

## story_96_no_greet_location_cuisine_price_with_email
* restaurant_search{"cuisine":"North Indian", "location":"Mysore", "price": "More than 700"}
  - slot{"location": "Mysore"}  
  - action_verify_location
  - slot{"location": "Mysore"}  
  - slot{"location_ok": true}  
  - slot{"cuisine": "North Indian"}
  - slot{"price": "More than 700"} 
  - action_search_restaurants
  - slot{"search_validity" : "invalid"}
  - utter_search_invalid
  - utter_goodbye
  - action_restart
  
## story_97_greet_location_cuisine_price_with_email
* greet
  - utter_greet
* restaurant_search{"cuisine":"North Indian", "location":"Mysore", "price": "More than 700"}
  - slot{"location": "Mysore"}  
  - action_verify_location
  - slot{"location": "Mysore"}  
  - slot{"location_ok": true}  
  - slot{"cuisine": "North Indian"}
  - slot{"price": "More than 700"} 
  - action_search_restaurants
  - slot{"search_validity" : "invalid"}
  - utter_search_invalid
  - utter_goodbye
  - action_restart

## story_98_no_greet_location_cuisine_budget_valid_no_email
* greet
  - utter_greet
* restaurant_search{"cuisine":"North Indian", "location":"Mysore", "price": "More than 700"}
  - slot{"location": "Mysore"}  
  - action_verify_location
  - slot{"location": "Mysore"}  
  - slot{"location_ok": true}  
  - slot{"cuisine": "North Indian"}
  - slot{"price": "More than 700"} 
  - action_search_restaurants
  - slot{"search_validity" : "invalid"}
  - utter_search_invalid
  - utter_goodbye
  - action_restart   
  
## story_99_location_invalid_retry_email_out_of_scope
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "York"}
  - slot{"location": "York"}  
  - action_verify_location
  - slot{"location": null}   
  - slot{"location_ok": false}    
  - action_slot_reset    
  - reset_slots    
  - utter_ask_location 
* restaurant_search{"location": "Bangalore"}
  - slot{"location": "Bangalore"}  
  - action_verify_location
  - slot{"location": "Bangalore"}  
  - slot{"location_ok": true}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - slot{"cuisine": "Chinese"}
  - utter_ask_price_range
* restaurant_search{"price": "Rs. 300 to 700"}   
  - slot{"price": "Rs. 300 to 700"}
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email
* out_of_scope
  - utter_ask_email
* deny
  - utter_goodbye
  - action_restart

## story_100_location_invalid_retry_email_out_of_scope
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "Farmington"}
  - slot{"location": "Farmington"}  
  - action_verify_location
  - slot{"location": null}   
  - slot{"location_ok": false}     
  - action_slot_reset    
  - reset_slots    
  - utter_ask_location 
* restaurant_search{"location": "Bangalore"}
  - slot{"location": "Bangalore"}  
  - action_verify_location
  - slot{"location": "Bangalore"}  
  - slot{"location_ok": true}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - slot{"cuisine": "Chinese"}
  - utter_ask_price_range
* restaurant_search{"price": "Rs. 300 to 700"}   
  - slot{"price": "Rs. 300 to 700"}
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email
* out_of_scope
  - utter_ask_email
* sendmail{"email": "tanyadayanand@gmail.com"}   
  - slot{"email": "tanyadayanand@gmail.com"}
  - action_send__mail
  - slot{"email": "tanyadayanand@gmail.com"}
  - utter_goodbye
  - action_restart

## story_101_location_invalid_out_of_scope
* restaurant_search{"location":"Simoga", "cuisine":"mexican"}
  - slot{"location": "Simoga"}  
  - action_verify_location
  - slot{"location": null}   
  - slot{"location_ok": false}     
  - action_slot_reset    
  - reset_slots    
  - utter_ask_location 
* out_of_scope
  - utter_goodbye
  - action_restart

## story_102_location_invalid_retry_email_out_of_scope
* restaurant_search{"location":"Simoga", "cuisine":"lebenese"}
  - slot{"location": "Simoga"}  
  - action_verify_location
  - slot{"location": null}   
  - slot{"location_ok": false}     
  - action_slot_reset    
  - reset_slots    
  - utter_ask_location 
* restaurant_search{"location": "Bangalore"}
  - slot{"location": "Bangalore"}  
  - action_verify_location
  - slot{"location": "Bangalore"}  
  - slot{"location_ok": true}
  - utter_ask_cuisine
* restaurant_search{"cuisine":"mexican"}
  - utter_ask_price_range
* restaurant_search{"price": "Rs. 300 to 700"}   
  - slot{"price": "Rs. 300 to 700"}
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email
* out_of_scope
  - utter_ask_email
* sendmail{"email": "tanyadayanand@gmail.com"}   
  - slot{"email": "tanyadayanand@gmail.com"}
  - action_send__mail
  - slot{"email": "tanyadayanand@gmail.com"}
  - utter_goodbye
  - action_restart

## story_103_location_invalid_retry_email_out_of_scope
* restaurant_search{"location":"Simoga", "cuisine":"lebenese"}
  - slot{"location": "Simoga"}  
  - action_verify_location
  - slot{"location": null}   
  - slot{"location_ok": false}     
  - action_slot_reset    
  - reset_slots    
  - utter_ask_location 
* restaurant_search{"location": "Bangalore"}
  - slot{"location": "Bangalore"}  
  - action_verify_location
  - slot{"location": "Bangalore"}  
  - slot{"location_ok": true}
  - utter_ask_cuisine
* restaurant_search{"cuisine":"mexican"}
  - utter_ask_price_range
* restaurant_search{"price": "Rs. 300 to 700"}   
  - slot{"price": "Rs. 300 to 700"}
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email
* out_of_scope
  - utter_ask_email
* deny
  - utter_goodbye
  - action_restart

## story_104_location_invalid_retry_email_out_of_scope
* restaurant_search{"location": "Bilaspur"}
  - slot{"location": "Bilaspur"}  
  - action_verify_location
  - slot{"location": null}   
  - slot{"location_ok": false}     
  - action_slot_reset    
  - reset_slots    
  - utter_ask_location 
* restaurant_search{"location": "Bangalore"}
  - slot{"location": "Bangalore"}  
  - action_verify_location
  - slot{"location": "Bangalore"}  
  - slot{"location_ok": true}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - slot{"cuisine": "Chinese"}
  - utter_ask_price_range
* restaurant_search{"price": "Rs. 300 to 700"}   
  - slot{"price": "Rs. 300 to 700"}
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email
* out_of_scope
  - utter_ask_email
* sendmail{"email": "tanyadayanand@gmail.com"}   
  - slot{"email": "tanyadayanand@gmail.com"}
  - action_send__mail
  - slot{"email": "tanyadayanand@gmail.com"}
  - utter_goodbye
  - action_restart

## story_105_location_invalid_retry_email_out_of_scope
* restaurant_search{"location": "Bilaspur"}
  - slot{"location": "Bilaspur"}  
  - action_verify_location
  - slot{"location": null}   
  - slot{"location_ok": false}     
  - action_slot_reset    
  - reset_slots    
  - utter_ask_location 
 * restaurant_search{"location": "Bangalore"}
  - slot{"location": "Bangalore"}  
  - action_verify_location
  - slot{"location": "Bangalore"}  
  - slot{"location_ok": true}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - slot{"cuisine": "Chinese"}
  - utter_ask_price_range
* restaurant_search{"price": "Rs. 300 to 700"}   
  - slot{"price": "Rs. 300 to 700"}
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email
* out_of_scope
  - utter_ask_email
* deny
  - utter_goodbye
  - action_restart

## story_106_cuisine_location_buget_valid_email_out_of_scope
* restaurant_search{"location":"Kolkata", "cuisine":"mexican"}
  - slot{"location": "Bijapur"}  
  - action_verify_location
  - slot{"location": "Kolkata"}  
  - slot{"location_ok": true}
  - slot{"cuisine": "Mexican"}
  - utter_ask_price_range
* restaurant_search{"price": "Rs. 300 to 700"}   
  - slot{"price": "Rs. 300 to 700"}
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email
* out_of_scope
  - utter_ask_email
* sendmail{"email": "tanyadayanand@gmail.com"}   
  - slot{"email": "tanyadayanand@gmail.com"}
  - action_send__mail
  - slot{"email": "tanyadayanand@gmail.com"}
  - utter_goodbye
  - action_restart

## story_107_cuisine_location_buget_valid_email_out_of_scope
* restaurant_search{"location":"Kolkata", "cuisine":"mexican"}
  - slot{"location": "Kolkata"}  
  - action_verify_location
  - slot{"location": "Kolkata"}  
  - slot{"location_ok": true}
  - slot{"cuisine": "Mexican"}
  - utter_ask_price_range
* restaurant_search{"price": "Rs. 300 to 700"}   
  - slot{"price": "Rs. 300 to 700"}
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email
* out_of_scope
  - utter_ask_email
* deny
  - utter_goodbye
  - action_restart
 
## story_108_location_out_of_scope_affirm  
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* out_of_scope
  - action_slot_reset
  - reset_slots    
  - utter_ask_location  
* restaurant_search{"location": "Bangalore"}
  - slot{"location": "Bangalore"}  
  - action_verify_location
  - slot{"location": "Bangalore"}  
  - slot{"location_ok": true}
  - utter_ask_cuisine  
* restaurant_search{"cuisine": "Chinese"} 
  - slot{"cuisine": "Chinese"}
  - utter_ask_price_range
* restaurant_search{"price": "Rs. 300 to 700"}    
  - slot{"price": "Rs. 300 to 700"}
  - action_search_restaurants
  - slot{"search_validity_ok" : true}
  - utter_ask_email
* sendmail{"email": "tanyadayanand@gmail.com"}   
  - slot{"email": "tanyadayanand@gmail.com"}
  - action_send__mail
  - slot{"email": "tanyadayanand@gmail.com"}
* thank
  - utter_goodbye
  - action_restart

  

  
