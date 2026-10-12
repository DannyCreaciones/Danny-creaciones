(() => {
  const products = window.DANNY_PRODUCTS || [];
  const money = n => new Intl.NumberFormat('es-AR',{style:'currency',currency:'ARS',maximumFractionDigits:0}).format(n || 0);
  let cart = JSON.parse(localStorage.getItem('dannyCart') || '{}');
  const $ = id => document.getElementById(id);
  const save = () => localStorage.setItem('dannyCart', JSON.stringify(cart));
  const count = () => Object.values(cart).reduce((a,b)=>a+b,0);
  const total = () => Object.entries(cart).reduce((sum,[id,qty])=>sum+(products.find(p=>p.id===Number(id))?.price || 0)*qty,0);
  function renderCart(){
    $('cartCount').textContent=count(); $('cartTotal').textContent=money(total());
    const items=$('cartItems');
    if(!count()){items.innerHTML='<p class="empty-cart">Todavía no agregaste productos.<br>Explorá la colección y elegí tus favoritos.</p>';return;}
    items.innerHTML=Object.entries(cart).filter(([,q])=>q>0).map(([id,qty])=>{const p=products.find(x=>x.id===Number(id));if(!p)return '';return `<div class="cart-row"><div><h3>${escapeHtml(p.name)}</h3><small>${money(p.price)} c/u</small><div class="qty-controls"><button data-qty="${p.id}" data-delta="-1" aria-label="Quitar uno">−</button><span>${qty}</span><button data-qty="${p.id}" data-delta="1" aria-label="Agregar uno">+</button></div></div><strong class="cart-row-price">${money(p.price*qty)}</strong></div>`}).join('');
  }
  function escapeHtml(s){return String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));}
  function add(id){cart[id]=(cart[id]||0)+1;save();renderCart();document.body.classList.add('cart-opened');$('cartDrawer').setAttribute('aria-hidden','false');}
  document.addEventListener('click',e=>{const b=e.target.closest('[data-add]');if(b){add(Number(b.dataset.add));return;}const q=e.target.closest('[data-qty]');if(q){const id=q.dataset.qty;cart[id]=(cart[id]||0)+Number(q.dataset.delta);if(cart[id]<=0)delete cart[id];save();renderCart();}});
  $('cartOpen').addEventListener('click',()=>{document.body.classList.add('cart-opened');$('cartDrawer').setAttribute('aria-hidden','false')});
  function closeCart(){document.body.classList.remove('cart-opened');$('cartDrawer').setAttribute('aria-hidden','true')}
  $('cartClose').addEventListener('click',closeCart);$('cartBackdrop').addEventListener('click',closeCart);
  $('clearCart').addEventListener('click',()=>{cart={};save();renderCart()});
  $('checkoutButton').addEventListener('click',()=>{if(!count()){alert('Primero agregá algún producto al carrito.');return;}const lines=Object.entries(cart).map(([id,qty])=>{const p=products.find(x=>x.id===Number(id));return p?`• ${p.name} x${qty} — ${money(p.price*qty)}`:''}).filter(Boolean);const msg=`Hola, Danny Creaciones. Quiero consultar por este pedido:\n\n${lines.join('\n')}\n\nTotal estimado: ${money(total())}\n\n¿Me confirman disponibilidad, precio final y entrega?`;window.open(`https://wa.me/${window.DANNY_WHATSAPP}?text=${encodeURIComponent(msg)}`,'_blank','noopener');});
  $('filters').addEventListener('click',e=>{const b=e.target.closest('[data-category]');if(!b)return;document.querySelectorAll('.filter').forEach(x=>x.classList.toggle('active',x===b));document.querySelectorAll('.product-card').forEach(c=>c.hidden=b.dataset.category!=='Todos'&&c.dataset.category!==b.dataset.category)});
  $('menuToggle').addEventListener('click',()=> $('mainNav').classList.toggle('open'));
  document.querySelectorAll('#mainNav a').forEach(a=>a.addEventListener('click',()=> $('mainNav').classList.remove('open')));
  document.addEventListener('keydown',e=>{if(e.key==='Escape')closeCart()});
  renderCart();
})();
