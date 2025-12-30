
// Cart Logic for MarketSite (Quote System)

const Cart = {
    key: 'marketsite_cart',

    getAll() {
        const stored = localStorage.getItem(this.key);
        return stored ? JSON.parse(stored) : [];
    },

    add(product) {
        const cart = this.getAll();
        const existing = cart.find(item => item.id === product.id);

        if (existing) {
            existing.quantity += product.quantity || 1;
        } else {
            cart.push({
                id: product.id,
                title: product.title,
                price: product.price, // Display string or value
                quantity: product.quantity || 1,
                url: product.url,
                image: product.image
            });
        }

        localStorage.setItem(this.key, JSON.stringify(cart));
        this.updateUI();
        this.showToast('Produto adicionado à cotação!');
    },

    remove(id) {
        let cart = this.getAll();
        cart = cart.filter(item => item.id !== id);
        localStorage.setItem(this.key, JSON.stringify(cart));
        this.updateUI();
    },

    updateQuantity(id, qty) {
        const cart = this.getAll();
        const item = cart.find(item => item.id === id);
        if (item) {
            item.quantity = parseInt(qty);
            if (item.quantity <= 0) {
                this.remove(id);
                return;
            }
            localStorage.setItem(this.key, JSON.stringify(cart));
            this.updateUI();
        }
    },

    clear() {
        localStorage.removeItem(this.key);
        this.updateUI();
    },

    totalItems() {
        return this.getAll().reduce((acc, item) => acc + item.quantity, 0);
    },

    updateUI() {
        const total = this.totalItems();
        const badges = document.querySelectorAll('.cart-count');
        badges.forEach(badge => {
            badge.textContent = total;
            badge.style.display = total > 0 ? 'flex' : 'none';
        });

        // Update Cart Page Table if exists
        const cartTableBody = document.getElementById('cart-items-body');
        if (cartTableBody) {
            this.renderCartPage(cartTableBody);
        }
    },

    renderCartPage(tbody) {
        const cart = this.getAll();
        tbody.innerHTML = '';

        if (cart.length === 0) {
            tbody.innerHTML = '<tr><td colspan="5" class="text-center">Sua cotação está vazia.</td></tr>';
            return;
        }

        cart.forEach(item => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td><img src="${item.image}" alt="${item.title}" style="width:50px; height:50px; object-fit:cover;"></td>
                <td><a href="${item.url}">${item.title}</a></td>
                <td>
                    <input type="number" min="1" value="${item.quantity}" 
                           onchange="Cart.updateQuantity('${item.id}', this.value)"
                           style="width: 60px; padding: 5px;">
                </td>
                <td>${item.price}</td>
                <td>
                    <button onclick="Cart.remove('${item.id}')" style="color:red; background:none; border:none; cursor:pointer;">&times;</button>
                </td>
            `;
            tbody.appendChild(tr);
        });
    },

    generateWhatsAppLink() {
        const cart = this.getAll();
        if (cart.length === 0) return '';

        let message = "*Olá, gostaria de solicitar um orçamento para os seguintes itens:*%0A%0A";
        cart.forEach(item => {
            message += `- ${item.quantity}x ${item.title}%0A`;
        });

        message += "%0A*Aguardo o retorno com preços e frete.*";
        return `https://wa.me/5511999999999?text=${message}`; // Replace with real number
    },

    showToast(msg) {
        // Simple toast implementation
        const div = document.createElement('div');
        div.textContent = msg;
        div.style.cssText = 'position:fixed; bottom:20px; right:20px; background:#333; color:#fff; padding:10px 20px; border-radius:4px; z-index:9999; animation: fadein 0.5s;';
        document.body.appendChild(div);
        setTimeout(() => div.remove(), 3000);
    }
};

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    Cart.updateUI();
});
