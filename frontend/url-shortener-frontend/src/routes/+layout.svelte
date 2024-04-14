<script>
	import '../app.css';
</script>

<div class="navbar bg-base-100">
  <div class="flex-1">
    <a class="btn btn-ghost text-xl" href="/">lit-short</a>
  </div>
  <!-- <div class="flex-none">
    <ul class="menu menu-horizontal px-1">
      <li><a>Short a Link</a></li>  
    </ul>
  </div> -->
</div>

<main class="container mx-auto p-16">
<slot />
</main>

<footer class="footer footer-center p-4 bg-base-300 text-base-content">
  <aside>
    <p>Copyright © 2024 - All right reserved by ACME Industries Ltd</p>
  </aside>
</footer>