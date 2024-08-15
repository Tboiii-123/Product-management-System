from django.shortcuts import render,get_object_or_404,redirect


from django.contrib.auth.decorators import login_required

from . models import Product, Product_detail

#To register we import
from django.contrib.auth.models import User

#For pop up messages
from django.contrib import messages

#For Authentification
from django.contrib.auth import authenticate,login ,logout

#For sending Emails
import smtplib



#Email and password for the server

emailName='lawalhussein775@gmail.com'
#make sure u delete your password before uploading to the github
passwordName ='your password'

              


             

#The welcome page
def index(request):


    
    return render(request,'welcome.html',{

            
    })




#The main page of the web
@login_required
def view(request):

    products=Product.objects.all()
    



    try:
                 

        if request.method == "POST":
                    
                    product_name =request.POST.get('item')
                    product = Product.objects.get(id=product_name)
                
                    product_price =float(request.POST.get('price'))
                    
                    
                    product_quantity = request.POST.get('quantity')
                    
                    product_quantity =int(product_quantity)

                    

                    
                    buyer_name =request.POST.get('bname')

                    buyer_number =request.POST.get('bnumber')

                    buyer_email =request.POST.get('bmail')

                    payment =request.POST.get('payment') == 'on'

                    price2 =request.POST.get('price2')

                    Total =request.POST.get('payment',product_price) * product_quantity

                    if request.POST.get('payment') == 'on':
                    
                        price_paid =request.POST.get('price',product_price) * product_quantity

                        
                        message = f"""Hello {buyer_name},
                        
                        \n\nThank you for your purchase.
                        
                        You have fully paid for the goods.
                        
                        \n\nTotal Amount Paid: ${price_paid}\n\nThank you for shopping with us!"""
        

                    else:
                        
                        price_paid =request.POST.get('price2',0) 
                        

                        price_owing =request.POST.get('owing',0)
                    
                    
                        message = f"""Hello {buyer_name},
                        
                        \nThank you for your purchase. Here are the details of your payment:
                        
                        \nTotal Cost: {Total}\nAmount Paid: {price2}\nAmount Owing: {price_owing}\n\nPlease complete the payment at your earliest convenience.\n\nThank you for shopping with us!"""

                    
                    
                    price_owing = float(request.POST.get('owing',0))


                    product_details =Product_detail.objects.create(
                        
                        name =product,

                        price =product_price * product_quantity,

                        quantity =product_quantity,

                        buyer_name =buyer_name,

                        buyer_number =buyer_number ,

                        payment_status =payment,
                        
                        buyer_email =buyer_email,
                        
                        price_paid =price_paid,
                        
                        price_owing =abs(price_owing),

                    )
                    
                    to_emailName =buyer_email
            
                    server =smtplib.SMTP('smtp.gmail.com', 587)
            
                    server.starttls()

                    server.login(emailName,passwordName)
            
            

                    server.sendmail(emailName,to_emailName,message)
                
                    server.quit()
                    
                
                    messages.success(request,('Item Purchaced successfully......'))


    except:
         
         messages.error(request,('There was an error trying to Purchase!!!'))


         

    return render(request,'view.html',{

        'product':products,
        

            
    })



#The login page
def login_user(request):



    if request.method == "POST":
         
         username =request.POST.get('user')

         password = request.POST.get('password')

         user =authenticate(username =username, password =password)

         
        
  
           

         if user is not None:


            login(request, user)
              
            fname =user.first_name
            lname =user.last_name


        #Email Connection
            Message = f"""

                                Dear {fname} {lname},

                    We wanted to inform you that you have successfully logged into the company portal.

                    Please remember to adhere to our company policies and ensure that our customers receive the best service possible.

                    Thank you for your hard work and dedication.

                    Best regards,
                    Hussein Store!!!
                    """
            to_emailName =user.email
        
            server =smtplib.SMTP('smtp.gmail.com', 587)
        
            server.starttls()

            server.login(emailName,passwordName)
        
          

            server.sendmail(emailName,to_emailName,Message)
            
            server.quit()
                            
            messages.success(request,(f"{ request.user} Logged in successfully....."))

            return redirect('view')


         else:
            messages.error(request,("There was an error logging in ......"))

            return redirect('login')
         
              


    return render(request,'login.html',{

    })


#Login out process and redirecting to the welcome Page
def logout_user(request):

    logout(request)

    messages.success(request,'Logged out sucessfully.....')


    return redirect('welcome')



#The register Page
def register_user(request):

    
    

    if request.method =="POST":

        firstname =request.POST.get('firstname')

        lastname =request.POST.get('lastname')
        
        username =request.POST.get('username')

        number  =request.POST.get('number')
        email =request.POST.get('email')

        code =request.POST.get('code')

        password1 =request.POST.get('password1')

        password2=request.POST.get('password2')
        company_code ='python'

        
        
         
        
        
        if firstname =='' or lastname =='' or username=='' or number =='' or number =='' or  email =='' or password1 =='' or password2 =='' or code =='':
             
            messages.error(request,("All Entry must be filled......"))
            redirect('register')

        else:
         

            if code == company_code:

                    if User.objects.filter(username =username).exists():

                        messages.error(request,("Sorry!!,there was a problem registering. Username already taken. Please try again...."))

                        redirect('register')

                    elif password1 != password2:
                        messages.error(request,("Sorry!!,please make sure your password matches...."))

                        return redirect('register')

                        

            
                    else :
                        try:
                                                    
                            user =  User.objects.create_user(username=username,
                                                             
                                                             first_name=firstname, 

                                                             last_name =lastname,

                                                               password=password1,

                                                               email=email
                                                               
                                                               )
                            fname =firstname
                            lname =lastname
                                
                            Message = f"""
                            Hi {fname} {lname},

                            Congratulations and welcome to Hussein Store! We are excited to have you join our team as a new employee.

                            As you begin your journey with us, we hope you give your best and contribute to our success. Please ensure to familiarize yourself with our company policies and procedures.

                            If you have any questions or need assistance, feel free to reach out to your manager or the HR department.

                            Best regards,
                            Hussein Store Team
                            """
                            
                            to_emailName =email



                            #Email Connection
                            
                            server =smtplib.SMTP('smtp.gmail.com', 587)
                            
                            server.starttls()

                            server.login(emailName,passwordName)


                            server.sendmail(emailName,to_emailName,Message)
                            


                            #login(request,user)

                            messages.success(request,("You have registered successfully as an Employee. Welcome......."))

                            return redirect('login')

                        except Exception as e:
                             messages.error(request, f"An error occurred: {str(e)}. Please try again.")
                             return redirect('register')

            else:
                    messages.error(request,("The code inserted is wrong, please insert the right code"))
                    return redirect('register')




    return render(request,'register.html',{

    })



#Updating the store Page
@login_required
def update(request,item):
     
     product =Product_detail.objects.get(id=item)

     
     

     try:

        if request.method == "POST":

        
            Total =product.price
            
            
            price_paid =request.POST.get('price')

            

            owing_amount =float(request.POST.get('owing'))
            #abs is used to convert a nagative number to a postiviev number
            owing_amount =abs(owing_amount)


            buyer_email =product.buyer_email


            
            if request.POST.get('payment_status') == 'on':
                 
                 product.price_paid =price_paid

                 product.price_owing =owing_amount
            
                 
                 product.payment_status = 'payment_status' in request.POST
            
                 product.save()
                 message = f"""Hello {product.buyer_name},
    
    \nThank you for your recent purchase. We are pleased to inform you that your payment has been fully received.
    
    \nThank you for shopping with us!
    """
            else:

                product.price_paid =price_paid

                product.price_owing =owing_amount
                
                product.save()
                
                message = f"""Hello {product.buyer_name},
    
    \nThank you for your recent purchase. Here are the details of your payment:
    
    \nTotal Cost: {Total}\nAmount Paid: {price_paid}\nAmount Owing: {owing_amount}\n\nPlease complete the payment at your earliest convenience.
    
    \nThank you for shopping with us!
    """
                


    
            to_emailName =buyer_email
    
            server =smtplib.SMTP('smtp.gmail.com', 587)
    
            server.starttls()

            server.login(emailName,passwordName)
    
    

            server.sendmail(emailName,to_emailName,message)
        
            server.quit()
                
                 
            messages.success(request,('Item Updated  successfully......'))
            
            return redirect('data_list')
                    
        
     except Exception :
        messages.error(request,("There is an error in updating the purchase ......"))
     
     return render(request,'update.html',{
          'product':product,
     })




#The store page where it shwows all the objects in the database
@login_required
def data_list(request):
     
     products =Product_detail.objects.all()

     return render(request,'store.html',{
          'products':products

          
     })



#For filtering the objects in the database by name Page
def searched_product(request):
            
               
        if request.method == "POST":
            
            searched =request.POST.get('searched')

            if searched =='all':
                products=Product_detail.objects.all()
            else:


                products =Product_detail.objects.filter(name__name__icontains=searched)
            

            
            return render(request,'searched.html',{
                
                'products':products,
                'searched': searched
                
                               
            })
    
        return render(request,'searched.html',{
                       
            
        })

     




'''
username
lawal

password
1234

email
lawalhussein775@gmail.com


'''