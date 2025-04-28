package second;

// Amishav Cohen

public class Main {

    // Class for A simple Mobile phone
    public static class MobilePhone {

        // the brand who made the phone (Apple, Samsung, Xiaomi)
        public String brand;
        // the model name (Galaxy S21, Iphone 13)
        public String model;
        // price in shekels
        public double price;

        // constructor that gets all properties and checks for negative price
        public MobilePhone(String brand, String model, double price) {
            this.brand = brand;
            this.model = model;
            // if price is negative warns through a print
            if (price < 0)
                System.out.println("price cannot be negative");
            else this.price = price;
        }

        // discounts the price based on a percentage given
        public void discount(double percentage){
            // if the price is negative, doesn't apply discount
            if (this.price < 0)
                System.out.println("This phone does not have a price");
            else
                this.price = this.price * (1-percentage/100);
        }

        // prints all the proprieties of the object
        public void printDetails(){
            System.out.println( "Brand: " + this.brand + ", Model: " + this.model +
                    ", Price: " + (this.price < 0 ? "None" : this.price));
        }

        // returns true only if the object is an instance of Mobile phone and the price is the same
        @Override
        public boolean equals(Object obj) {
            return obj instanceof MobilePhone && ((MobilePhone) obj).price == this.price;
        }
    }

    public static void main(String[] args) {

        MobilePhone phone1 = new MobilePhone("Samsung", "Galaxy S21", 2200d);
        MobilePhone phone2 = new MobilePhone("Apple", "Iphone 14+", 1900d);

        System.out.println("Phone 1:");
        phone1.printDetails();
        System.out.println("\nPhone 2:");
        phone2.printDetails();

        phone1.discount(13d);
        phone2.discount(24d);

        System.out.println("\nDiscounted: ");
        System.out.println("Phone 1:");
        phone1.printDetails();
        System.out.println("\nPhone 2:");
        phone2.printDetails();

    }

}
