---
id: 'Banner'
section: components
cssPrefix: pf-v6-c-banner
---## Examples

### Basic

Banners can be styled with one of 9 different nonstatus colors. A nonstatus banner should only be used when the banner color does not represent status or severity.

```html
<div class="pf-v6-c-banner">Default banner</div>

<br />

<div class="pf-v6-c-banner pf-m-red">Red banner</div>

<br />

<div class="pf-v6-c-banner pf-m-orangered">Orangered banner</div>

<br />

<div class="pf-v6-c-banner pf-m-orange">Orange banner</div>

<br />

<div class="pf-v6-c-banner pf-m-yellow">Yellow banner</div>

<br />

<div class="pf-v6-c-banner pf-m-green">Green banner</div>

<br />

<div class="pf-v6-c-banner pf-m-teal">Teal banner</div>

<br />

<div class="pf-v6-c-banner pf-m-blue">Blue banner</div>

<br />

<div class="pf-v6-c-banner pf-m-purple">Purple banner</div>

```

### Banner with links

```html
<div class="pf-v6-c-banner">
  Default banner with a
  <a
    href="https://www.w3.org/TR/WCAG20-TECHS/ARIA8.html#ARIA8-examples"
  >link</a>
</div>
<br />
<div class="pf-v6-c-banner">
  Default banner with a
  <a
    class="pf-m-disabled"
    role="link"
    aria-disabled="true"
  >disabled link</a>
</div>
<br />
<div class="pf-v6-c-banner pf-m-blue">
  Blue banner with an
  <button
    class="pf-v6-c-button pf-m-inline pf-m-link"
    type="button"
  >
    <span class="pf-v6-c-button__text">inline link button</span>
  </button>
</div>
<br />
<div class="pf-v6-c-banner pf-m-yellow">
  Yellow banner with an
  <a
    class="pf-v6-c-button pf-m-inline pf-m-link"
    href="https://www.w3.org/TR/WCAG20-TECHS/ARIA8.html#ARIA8-examples"
  >
    <span class="pf-v6-c-button__text">inline link button (anchor)</span>
  </a>
</div>
<br />
<div class="pf-v6-c-banner pf-m-red">
  Red banner with a
  <button
    class="pf-v6-c-button pf-m-inline pf-m-link"
    type="button"
    disabled
  >
    <span class="pf-v6-c-button__text">disabled inline link button</span>
  </button>
</div>

```

### Status

When a banner is used to convey status, it is advised to add an icon that also conveys status visually, and to provide screen reader text using `.pf-v6-screen-reader` or an equivalent.

```html
<div class="pf-v6-c-banner pf-m-success">
  <div class="pf-v6-l-flex pf-m-space-items-sm">
    <div class="pf-v6-l-flex__item">
      <span class="pf-v6-screen-reader">Success banner:</span>

      <svg
        class="pf-v6-svg"
        viewBox="0 0 32 32"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm7.795 11.795-8.646 8.646c-.317.317-.733.475-1.149.475s-.832-.158-1.149-.475l-4.646-4.646a1.126 1.126 0 0 1 1.591-1.591l4.205 4.205 8.205-8.205a1.126 1.126 0 0 1 1.591 1.591Z"
        />
      </svg>
    </div>
    <div class="pf-v6-l-flex__item">Success banner</div>
  </div>
</div>

<br />

<div class="pf-v6-c-banner pf-m-warning">
  <div class="pf-v6-l-flex pf-m-space-items-sm">
    <div class="pf-v6-l-flex__item">
      <span class="pf-v6-screen-reader">Warning banner:</span>

      <svg
        class="pf-v6-svg"
        viewBox="0 0 32 32"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="m31.874 28.514-15.011-27a1.001 1.001 0 0 0-1.748 0l-15.011 27A1 1 0 0 0 .978 30H31a1 1 0 0 0 .874-1.486ZM14.5 12a1.5 1.5 0 0 1 3 0v5a1.5 1.5 0 0 1-3 0v-5ZM16 26.001a2 2 0 1 1-.001-3.999A2 2 0 0 1 16 26.001Z"
        />
      </svg>
    </div>
    <div class="pf-v6-l-flex__item">Warning banner</div>
  </div>
</div>

<br />

<div class="pf-v6-c-banner pf-m-danger">
  <div class="pf-v6-l-flex pf-m-space-items-sm">
    <div class="pf-v6-l-flex__item">
      <span class="pf-v6-screen-reader">Danger banner:</span>

      <svg
        class="pf-v6-svg"
        viewBox="0 0 32 32"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm-1.5 8a1.5 1.5 0 1 1 3 0v7a1.5 1.5 0 1 1-3 0V9ZM16 25.001a2 2 0 1 1-.001-3.999A2 2 0 0 1 16 25.001Z"
        />
      </svg>
    </div>
    <div class="pf-v6-l-flex__item">Danger banner</div>
  </div>
</div>

<br />

<div class="pf-v6-c-banner pf-m-info">
  <div class="pf-v6-l-flex pf-m-space-items-sm">
    <div class="pf-v6-l-flex__item">
      <span class="pf-v6-screen-reader">Custom status banner:</span>

      <svg
        class="pf-v6-svg"
        viewBox="0 0 32 32"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm1.5 22a1.5 1.5 0 1 1-3 0v-5.157l-.188.04a1.5 1.5 0 0 1-.625-2.934l1.956-.416c.112-.024.223-.032.333-.03l.024-.002a1.5 1.5 0 0 1 1.5 1.5v7Zm-.08-12.58c-.38.37-.89.58-1.42.58a1.998 1.998 0 0 1-1.851-2.76c.051-.13.11-.24.19-.35.07-.11.15-.21.25-.3.74-.75 2.08-.75 2.83 0 .09.09.17.19.24.3.08.11.14.22.189.35.05.12.09.24.11.37.03.13.04.26.04.39 0 .53-.21 1.04-.58 1.42Z"
        />
      </svg>
    </div>
    <div class="pf-v6-l-flex__item">Info banner</div>
  </div>
</div>

<br />

<div class="pf-v6-c-banner pf-m-custom">
  <div class="pf-v6-l-flex pf-m-space-items-sm">
    <div class="pf-v6-l-flex__item">
      <span class="pf-v6-screen-reader">Custom status banner:</span>

      <svg
        class="pf-v6-svg"
        viewBox="0 0 32 32"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M28.75 22v3.5c0 .689-.561 1.25-1.25 1.25h-7.521c.005.084.021.166.021.25 0 2.206-1.794 4-4 4s-4-1.794-4-4c0-.084.016-.166.021-.25H4.5c-.689 0-1.25-.561-1.25-1.25V22a.75.75 0 0 1 .75-.75c1.24 0 2.25-1.009 2.25-2.25v-4c0-4.826 3.528-8.833 8.138-9.605A2.482 2.482 0 0 1 13.5 3.5C13.5 2.122 14.621 1 16 1s2.5 1.122 2.5 2.5c0 .761-.349 1.436-.888 1.895 4.61.772 8.138 4.779 8.138 9.605v4c0 1.241 1.01 2.25 2.25 2.25a.75.75 0 0 1 .75.75Z"
        />
      </svg>
    </div>
    <div class="pf-v6-l-flex__item">Custom banner</div>
  </div>
</div>

```

### Pill

To display a banner with rounded corners, use `pf-m-pill`. The pill modifier can be combined with any Banner modifier.

```html
<div class="pf-v6-c-banner pf-m-pill pf-m-success">
  <div class="pf-v6-l-flex pf-m-space-items-sm">
    <div class="pf-v6-l-flex__item">
      <span class="pf-v6-screen-reader">Success banner:</span>

      <svg
        class="pf-v6-svg"
        viewBox="0 0 32 32"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm7.795 11.795-8.646 8.646c-.317.317-.733.475-1.149.475s-.832-.158-1.149-.475l-4.646-4.646a1.126 1.126 0 0 1 1.591-1.591l4.205 4.205 8.205-8.205a1.126 1.126 0 0 1 1.591 1.591Z"
        />
      </svg>
    </div>
    <div class="pf-v6-l-flex__item">Success banner</div>
  </div>
</div>

<br />

<div class="pf-v6-c-banner pf-m-pill pf-m-warning">
  <div class="pf-v6-l-flex pf-m-space-items-sm">
    <div class="pf-v6-l-flex__item">
      <span class="pf-v6-screen-reader">Warning banner:</span>

      <svg
        class="pf-v6-svg"
        viewBox="0 0 32 32"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="m31.874 28.514-15.011-27a1.001 1.001 0 0 0-1.748 0l-15.011 27A1 1 0 0 0 .978 30H31a1 1 0 0 0 .874-1.486ZM14.5 12a1.5 1.5 0 0 1 3 0v5a1.5 1.5 0 0 1-3 0v-5ZM16 26.001a2 2 0 1 1-.001-3.999A2 2 0 0 1 16 26.001Z"
        />
      </svg>
    </div>
    <div class="pf-v6-l-flex__item">Warning banner</div>
  </div>
</div>

<br />

<div class="pf-v6-c-banner pf-m-pill pf-m-danger">
  <div class="pf-v6-l-flex pf-m-space-items-sm">
    <div class="pf-v6-l-flex__item">
      <span class="pf-v6-screen-reader">Danger banner:</span>

      <svg
        class="pf-v6-svg"
        viewBox="0 0 32 32"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm-1.5 8a1.5 1.5 0 1 1 3 0v7a1.5 1.5 0 1 1-3 0V9ZM16 25.001a2 2 0 1 1-.001-3.999A2 2 0 0 1 16 25.001Z"
        />
      </svg>
    </div>
    <div class="pf-v6-l-flex__item">Danger banner</div>
  </div>
</div>

<br />

<div class="pf-v6-c-banner pf-m-pill pf-m-info">
  <div class="pf-v6-l-flex pf-m-space-items-sm">
    <div class="pf-v6-l-flex__item">
      <span class="pf-v6-screen-reader">Custom status banner:</span>

      <svg
        class="pf-v6-svg"
        viewBox="0 0 32 32"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm1.5 22a1.5 1.5 0 1 1-3 0v-5.157l-.188.04a1.5 1.5 0 0 1-.625-2.934l1.956-.416c.112-.024.223-.032.333-.03l.024-.002a1.5 1.5 0 0 1 1.5 1.5v7Zm-.08-12.58c-.38.37-.89.58-1.42.58a1.998 1.998 0 0 1-1.851-2.76c.051-.13.11-.24.19-.35.07-.11.15-.21.25-.3.74-.75 2.08-.75 2.83 0 .09.09.17.19.24.3.08.11.14.22.189.35.05.12.09.24.11.37.03.13.04.26.04.39 0 .53-.21 1.04-.58 1.42Z"
        />
      </svg>
    </div>
    <div class="pf-v6-l-flex__item">Info banner</div>
  </div>
</div>

<br />

<div class="pf-v6-c-banner pf-m-pill pf-m-custom">
  <div class="pf-v6-l-flex pf-m-space-items-sm">
    <div class="pf-v6-l-flex__item">
      <span class="pf-v6-screen-reader">Custom status banner:</span>

      <svg
        class="pf-v6-svg"
        viewBox="0 0 32 32"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M28.75 22v3.5c0 .689-.561 1.25-1.25 1.25h-7.521c.005.084.021.166.021.25 0 2.206-1.794 4-4 4s-4-1.794-4-4c0-.084.016-.166.021-.25H4.5c-.689 0-1.25-.561-1.25-1.25V22a.75.75 0 0 1 .75-.75c1.24 0 2.25-1.009 2.25-2.25v-4c0-4.826 3.528-8.833 8.138-9.605A2.482 2.482 0 0 1 13.5 3.5C13.5 2.122 14.621 1 16 1s2.5 1.122 2.5 2.5c0 .761-.349 1.436-.888 1.895 4.61.772 8.138 4.779 8.138 9.605v4c0 1.241 1.01 2.25 2.25 2.25a.75.75 0 0 1 .75.75Z"
        />
      </svg>
    </div>
    <div class="pf-v6-l-flex__item">Custom banner</div>
  </div>
</div>

```

## Documentation

### Usage

| Class | Applied to | Outcome |
| -- | -- | -- |
| `.pf-v6-c-banner` | `<div>` |  Initiates a banner. **Required** |
| `.pf-m-red` | `.pf-v6-c-banner` |  Modifies banner for red styling. |
| `.pf-m-orangered` | `.pf-v6-c-banner` |  Modifies banner for orangered styling. |
| `.pf-m-orange` | `.pf-v6-c-banner` |  Modifies banner for orange styling. |
| `.pf-m-yellow` | `.pf-v6-c-banner` |  Modifies banner for yellow styling. |
| `.pf-m-green` | `.pf-v6-c-banner` |  Modifies banner for green styling. |
| `.pf-m-teal` | `.pf-v6-c-banner` |  Modifies banner for teal styling. |
| `.pf-m-blue` | `.pf-v6-c-banner` |  Modifies banner for blue styling. |
| `.pf-m-purple` | `.pf-v6-c-banner` |  Modifies banner for purple styling. |
| `.pf-m-success` | `.pf-v6-c-banner` |  Modifies banner for success status styling. |
| `.pf-m-warning` | `.pf-v6-c-banner` |  Modifies banner for warning status styling. |
| `.pf-m-danger` | `.pf-v6-c-banner` |  Modifies banner for danger status styling. |
| `.pf-m-info` | `.pf-v6-c-banner` |  Modifies banner for info status styling. |
| `.pf-m-custom` | `.pf-v6-c-banner` |  Modifies banner for custom status styling. |
| `.pf-m-sticky` | `.pf-v6-c-banner` |  Modifies banner to be sticky to the top of its container. |
| `.pf-m-pill` | `.pf-v6-c-banner` |  Modifies banner for pill styles. |
