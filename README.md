## Simple Ecommerce Backend using flask & google-cloud-firestore

Available on https://i-shop-api.herokuapp.com

# Usage


 <table>
        <thead>
            <tr>
                <td>#</td>
                <td>METHOD</td>
                <td>ENDPOINT</td>
                <td>PARAMETERS</td>
                <td>USE</td>
            </tr>
            <tr>
                <td>1</td>
                <td>GET</td>
                <td>/api/products</td>
                <td></td>
                <td>List All products in the store</td>
            </tr>
            <tr>
                <td>2</td>
                <td>POST</td>
                <td>/api/products</td>
                <td>
                    <ul>
                        <li>category [String]- Comma seperated for multiple values </li>
                        <li>product_name [String]</li>
                        <li>description - [String]</li>
                        <li>product_price - [Float]</li>
                        <li>img_urls - [String]- Comma seperated for multiple URLS</li>
                        <li>currency - [String]</li>
                        <li>quantity - [Int]</li>
                    </u>
                </td>
                <td>Adds a product into the store</td>
            </tr>
        </thead>
    </table>
