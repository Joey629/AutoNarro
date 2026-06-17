---
id: Pagination
section: components
cssPrefix: pf-v6-c-pagination
---## Examples

### Top

```html
<div class="pf-v6-c-pagination">
  <div class="pf-v6-c-pagination__total-items">
    <b>1 - 10</b>&nbsp;of&nbsp;
    <b>36</b>
  </div>
  <div class="pf-v6-c-pagination__page-menu">
    <button
      class="pf-v6-c-menu-toggle pf-m-text pf-m-plain"
      type="button"
      aria-expanded="false"
      id="pagination-menu-toggle-top-example"
    >
      <span class="pf-v6-c-menu-toggle__text">
        <b>1 - 10</b>&nbsp;of&nbsp;
        <b>36</b>
      </span>
      <span class="pf-v6-c-menu-toggle__controls">
        <span class="pf-v6-c-menu-toggle__toggle-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 20 20"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
            />
          </svg>
        </span>
      </span>
    </button>
  </div>
  <nav
    class="pf-v6-c-pagination__nav"
    aria-label="Pagination nav - top example"
  >
    <div class="pf-v6-c-pagination__nav-control pf-m-first">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Go to first page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 448 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M223.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L319.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L393.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34zm-192 34l136 136c9.4 9.4 24.6 9.4 33.9 0l22.6-22.6c9.4-9.4 9.4-24.6 0-33.9L127.9 256l96.4-96.4c9.4-9.4 9.4-24.6 0-33.9L201.7 103c-9.4-9.4-24.6-9.4-33.9 0l-136 136c-9.5 9.4-9.5 24.6-.1 34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-pagination__nav-control pf-m-prev">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Go to previous page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 256 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M31.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L127.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L201.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-pagination__nav-page-select">
      <span class="pf-v6-c-form-control">
        <input
          aria-label="Current page"
          type="number"
          min="1"
          max="4"
          value="1"
        />
      </span>
      <span aria-hidden="true">of 4</span>
    </div>
    <div class="pf-v6-c-pagination__nav-control pf-m-next">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Go to next page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 256 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-pagination__nav-control pf-m-last">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Go to last page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 448 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34zm192-34l-136-136c-9.4-9.4-24.6-9.4-33.9 0l-22.6 22.6c-9.4 9.4-9.4 24.6 0 33.9l96.4 96.4-96.4 96.4c-9.4 9.4-9.4 24.6 0 33.9l22.6 22.6c9.4 9.4 24.6 9.4 33.9 0l136-136c9.4-9.2 9.4-24.4 0-33.8z"
            />
          </svg>
        </span>
      </button>
    </div>
  </nav>
</div>

```

### Top sticky

```html
<div class="pf-v6-c-pagination pf-m-sticky">
  <div class="pf-v6-c-pagination__total-items">
    <b>1 - 10</b>&nbsp;of&nbsp;
    <b>36</b>
  </div>
  <div class="pf-v6-c-pagination__page-menu">
    <button
      class="pf-v6-c-menu-toggle pf-m-text pf-m-plain"
      type="button"
      aria-expanded="false"
      id="pagination-menu-toggle-top-sticky-example"
    >
      <span class="pf-v6-c-menu-toggle__text">
        <b>1 - 10</b>&nbsp;of&nbsp;
        <b>36</b>
      </span>
      <span class="pf-v6-c-menu-toggle__controls">
        <span class="pf-v6-c-menu-toggle__toggle-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 20 20"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
            />
          </svg>
        </span>
      </span>
    </button>
  </div>
  <nav
    class="pf-v6-c-pagination__nav"
    aria-label="Pagination nav - top sticky example"
  >
    <div class="pf-v6-c-pagination__nav-control pf-m-first">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Go to first page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 448 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M223.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L319.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L393.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34zm-192 34l136 136c9.4 9.4 24.6 9.4 33.9 0l22.6-22.6c9.4-9.4 9.4-24.6 0-33.9L127.9 256l96.4-96.4c9.4-9.4 9.4-24.6 0-33.9L201.7 103c-9.4-9.4-24.6-9.4-33.9 0l-136 136c-9.5 9.4-9.5 24.6-.1 34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-pagination__nav-control pf-m-prev">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Go to previous page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 256 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M31.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L127.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L201.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-pagination__nav-page-select">
      <span class="pf-v6-c-form-control">
        <input
          aria-label="Current page"
          type="number"
          min="1"
          max="4"
          value="1"
        />
      </span>
      <span aria-hidden="true">of 4</span>
    </div>
    <div class="pf-v6-c-pagination__nav-control pf-m-next">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Go to next page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 256 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-pagination__nav-control pf-m-last">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Go to last page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 448 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34zm192-34l-136-136c-9.4-9.4-24.6-9.4-33.9 0l-22.6 22.6c-9.4 9.4-9.4 24.6 0 33.9l96.4 96.4-96.4 96.4c-9.4 9.4-9.4 24.6 0 33.9l22.6 22.6c9.4 9.4 24.6 9.4 33.9 0l136-136c9.4-9.2 9.4-24.4 0-33.8z"
            />
          </svg>
        </span>
      </button>
    </div>
  </nav>
</div>
<div>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus pretium est a porttitor vehicula. Quisque vel commodo urna. Morbi mattis rutrum ante, id vehicula ex accumsan ut. Morbi viverra, eros vel porttitor facilisis, eros purus aliquet erat, nec lobortis felis elit pulvinar sem. Vivamus vulputate, risus eget commodo eleifend, eros nibh porta quam, vitae lacinia leo libero at magna. Maecenas aliquam sagittis orci, et posuere nisi ultrices sit amet. Aliquam ex odio, malesuada sed posuere quis, pellentesque at mauris. Phasellus venenatis massa ex, eget pulvinar libero auctor pretium. Aliquam erat volutpat. Duis euismod justo in quam ullamcorper, in commodo massa vulputate.</div>
<br />
<br />
<div>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus pretium est a porttitor vehicula. Quisque vel commodo urna. Morbi mattis rutrum ante, id vehicula ex accumsan ut. Morbi viverra, eros vel porttitor facilisis, eros purus aliquet erat, nec lobortis felis elit pulvinar sem. Vivamus vulputate, risus eget commodo eleifend, eros nibh porta quam, vitae lacinia leo libero at magna. Maecenas aliquam sagittis orci, et posuere nisi ultrices sit amet. Aliquam ex odio, malesuada sed posuere quis, pellentesque at mauris. Phasellus venenatis massa ex, eget pulvinar libero auctor pretium. Aliquam erat volutpat. Duis euismod justo in quam ullamcorper, in commodo massa vulputate.</div>
<br />
<br />
<div>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus pretium est a porttitor vehicula. Quisque vel commodo urna. Morbi mattis rutrum ante, id vehicula ex accumsan ut. Morbi viverra, eros vel porttitor facilisis, eros purus aliquet erat, nec lobortis felis elit pulvinar sem. Vivamus vulputate, risus eget commodo eleifend, eros nibh porta quam, vitae lacinia leo libero at magna. Maecenas aliquam sagittis orci, et posuere nisi ultrices sit amet. Aliquam ex odio, malesuada sed posuere quis, pellentesque at mauris. Phasellus venenatis massa ex, eget pulvinar libero auctor pretium. Aliquam erat volutpat. Duis euismod justo in quam ullamcorper, in commodo massa vulputate.</div>
<br />
<br />
<div>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus pretium est a porttitor vehicula. Quisque vel commodo urna. Morbi mattis rutrum ante, id vehicula ex accumsan ut. Morbi viverra, eros vel porttitor facilisis, eros purus aliquet erat, nec lobortis felis elit pulvinar sem. Vivamus vulputate, risus eget commodo eleifend, eros nibh porta quam, vitae lacinia leo libero at magna. Maecenas aliquam sagittis orci, et posuere nisi ultrices sit amet. Aliquam ex odio, malesuada sed posuere quis, pellentesque at mauris. Phasellus venenatis massa ex, eget pulvinar libero auctor pretium. Aliquam erat volutpat. Duis euismod justo in quam ullamcorper, in commodo massa vulputate.</div>

```

### Indeterminate (item count is not known)

```html
<div class="pf-v6-c-pagination">
  <div class="pf-v6-c-pagination__total-items">
    <b>1 - 10</b>&nbsp;of&nbsp;
    <b>many</b>
  </div>
  <div class="pf-v6-c-pagination__page-menu">
    <button
      class="pf-v6-c-menu-toggle pf-m-text pf-m-plain"
      type="button"
      aria-expanded="false"
      id="pagination-menu-toggle-top-indeterminate-example"
    >
      <span class="pf-v6-c-menu-toggle__text">
        <b>1 - 10</b>&nbsp;of&nbsp;
        <b>many</b>
      </span>
      <span class="pf-v6-c-menu-toggle__controls">
        <span class="pf-v6-c-menu-toggle__toggle-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 20 20"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
            />
          </svg>
        </span>
      </span>
    </button>
  </div>
  <nav
    class="pf-v6-c-pagination__nav"
    aria-label="Pagination nav - indeterminate item count example"
  >
    <div class="pf-v6-c-pagination__nav-control pf-m-first">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Go to first page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 448 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M223.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L319.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L393.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34zm-192 34l136 136c9.4 9.4 24.6 9.4 33.9 0l22.6-22.6c9.4-9.4 9.4-24.6 0-33.9L127.9 256l96.4-96.4c9.4-9.4 9.4-24.6 0-33.9L201.7 103c-9.4-9.4-24.6-9.4-33.9 0l-136 136c-9.5 9.4-9.5 24.6-.1 34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-pagination__nav-control pf-m-prev">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Go to previous page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 256 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M31.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L127.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L201.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-pagination__nav-page-select">
      <span class="pf-v6-c-form-control">
        <input
          aria-label="Current page"
          type="number"
          min="1"
          max="4"
          value="1"
        />
      </span>
    </div>
    <div class="pf-v6-c-pagination__nav-control pf-m-next">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Go to next page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 256 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-pagination__nav-control pf-m-last">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Go to last page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 448 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34zm192-34l-136-136c-9.4-9.4-24.6-9.4-33.9 0l-22.6 22.6c-9.4 9.4-9.4 24.6 0 33.9l96.4 96.4-96.4 96.4c-9.4 9.4-9.4 24.6 0 33.9l22.6 22.6c9.4 9.4 24.6 9.4 33.9 0l136-136c9.4-9.2 9.4-24.4 0-33.8z"
            />
          </svg>
        </span>
      </button>
    </div>
  </nav>
</div>

```

### Bottom

```html
<div>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus pretium est a porttitor vehicula. Quisque vel commodo urna. Morbi mattis rutrum ante, id vehicula ex accumsan ut. Morbi viverra, eros vel porttitor facilisis, eros purus aliquet erat, nec lobortis felis elit pulvinar sem. Vivamus vulputate, risus eget commodo eleifend, eros nibh porta quam, vitae lacinia leo libero at magna. Maecenas aliquam sagittis orci, et posuere nisi ultrices sit amet. Aliquam ex odio, malesuada sed posuere quis, pellentesque at mauris. Phasellus venenatis massa ex, eget pulvinar libero auctor pretium. Aliquam erat volutpat. Duis euismod justo in quam ullamcorper, in commodo massa vulputate.</div>
<br />
<br />
<div>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus pretium est a porttitor vehicula. Quisque vel commodo urna. Morbi mattis rutrum ante, id vehicula ex accumsan ut. Morbi viverra, eros vel porttitor facilisis, eros purus aliquet erat, nec lobortis felis elit pulvinar sem. Vivamus vulputate, risus eget commodo eleifend, eros nibh porta quam, vitae lacinia leo libero at magna. Maecenas aliquam sagittis orci, et posuere nisi ultrices sit amet. Aliquam ex odio, malesuada sed posuere quis, pellentesque at mauris. Phasellus venenatis massa ex, eget pulvinar libero auctor pretium. Aliquam erat volutpat. Duis euismod justo in quam ullamcorper, in commodo massa vulputate.</div>
<br />
<br />
<div>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus pretium est a porttitor vehicula. Quisque vel commodo urna. Morbi mattis rutrum ante, id vehicula ex accumsan ut. Morbi viverra, eros vel porttitor facilisis, eros purus aliquet erat, nec lobortis felis elit pulvinar sem. Vivamus vulputate, risus eget commodo eleifend, eros nibh porta quam, vitae lacinia leo libero at magna. Maecenas aliquam sagittis orci, et posuere nisi ultrices sit amet. Aliquam ex odio, malesuada sed posuere quis, pellentesque at mauris. Phasellus venenatis massa ex, eget pulvinar libero auctor pretium. Aliquam erat volutpat. Duis euismod justo in quam ullamcorper, in commodo massa vulputate.</div>
<br />
<br />
<div>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus pretium est a porttitor vehicula. Quisque vel commodo urna. Morbi mattis rutrum ante, id vehicula ex accumsan ut. Morbi viverra, eros vel porttitor facilisis, eros purus aliquet erat, nec lobortis felis elit pulvinar sem. Vivamus vulputate, risus eget commodo eleifend, eros nibh porta quam, vitae lacinia leo libero at magna. Maecenas aliquam sagittis orci, et posuere nisi ultrices sit amet. Aliquam ex odio, malesuada sed posuere quis, pellentesque at mauris. Phasellus venenatis massa ex, eget pulvinar libero auctor pretium. Aliquam erat volutpat. Duis euismod justo in quam ullamcorper, in commodo massa vulputate.</div>
<div class="pf-v6-c-pagination pf-m-bottom">
  <div class="pf-v6-c-pagination__page-menu">
    <button
      class="pf-v6-c-menu-toggle pf-m-top pf-m-text pf-m-plain"
      type="button"
      aria-expanded="false"
      id="pagination-menu-toggle-bottom-example"
    >
      <span class="pf-v6-c-menu-toggle__text">
        <b>1 - 10</b>&nbsp;of&nbsp;
        <b>36</b>
      </span>
      <span class="pf-v6-c-menu-toggle__controls">
        <span class="pf-v6-c-menu-toggle__toggle-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 20 20"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
            />
          </svg>
        </span>
      </span>
    </button>
  </div>
  <nav
    class="pf-v6-c-pagination__nav"
    aria-label="Pagination nav - bottom example"
  >
    <div class="pf-v6-c-pagination__nav-control pf-m-first">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Go to first page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 448 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M223.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L319.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L393.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34zm-192 34l136 136c9.4 9.4 24.6 9.4 33.9 0l22.6-22.6c9.4-9.4 9.4-24.6 0-33.9L127.9 256l96.4-96.4c9.4-9.4 9.4-24.6 0-33.9L201.7 103c-9.4-9.4-24.6-9.4-33.9 0l-136 136c-9.5 9.4-9.5 24.6-.1 34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-pagination__nav-control pf-m-prev">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Go to previous page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 256 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M31.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L127.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L201.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-pagination__nav-page-select">
      <span class="pf-v6-c-form-control">
        <input
          aria-label="Current page"
          type="number"
          min="1"
          max="4"
          value="1"
        />
      </span>
      <span aria-hidden="true">of 4</span>
    </div>
    <div class="pf-v6-c-pagination__nav-control pf-m-next">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Go to next page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 256 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-pagination__nav-control pf-m-last">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Go to last page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 448 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34zm192-34l-136-136c-9.4-9.4-24.6-9.4-33.9 0l-22.6 22.6c-9.4 9.4-9.4 24.6 0 33.9l96.4 96.4-96.4 96.4c-9.4 9.4-9.4 24.6 0 33.9l22.6 22.6c9.4 9.4 24.6 9.4 33.9 0l136-136c9.4-9.2 9.4-24.4 0-33.8z"
            />
          </svg>
        </span>
      </button>
    </div>
  </nav>
</div>

```

### Bottom plain

```html
<div>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus pretium est a porttitor vehicula. Quisque vel commodo urna. Morbi mattis rutrum ante, id vehicula ex accumsan ut. Morbi viverra, eros vel porttitor facilisis, eros purus aliquet erat, nec lobortis felis elit pulvinar sem. Vivamus vulputate, risus eget commodo eleifend, eros nibh porta quam, vitae lacinia leo libero at magna. Maecenas aliquam sagittis orci, et posuere nisi ultrices sit amet. Aliquam ex odio, malesuada sed posuere quis, pellentesque at mauris. Phasellus venenatis massa ex, eget pulvinar libero auctor pretium. Aliquam erat volutpat. Duis euismod justo in quam ullamcorper, in commodo massa vulputate.</div>
<br />
<br />
<div>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus pretium est a porttitor vehicula. Quisque vel commodo urna. Morbi mattis rutrum ante, id vehicula ex accumsan ut. Morbi viverra, eros vel porttitor facilisis, eros purus aliquet erat, nec lobortis felis elit pulvinar sem. Vivamus vulputate, risus eget commodo eleifend, eros nibh porta quam, vitae lacinia leo libero at magna. Maecenas aliquam sagittis orci, et posuere nisi ultrices sit amet. Aliquam ex odio, malesuada sed posuere quis, pellentesque at mauris. Phasellus venenatis massa ex, eget pulvinar libero auctor pretium. Aliquam erat volutpat. Duis euismod justo in quam ullamcorper, in commodo massa vulputate.</div>
<br />
<br />
<div>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus pretium est a porttitor vehicula. Quisque vel commodo urna. Morbi mattis rutrum ante, id vehicula ex accumsan ut. Morbi viverra, eros vel porttitor facilisis, eros purus aliquet erat, nec lobortis felis elit pulvinar sem. Vivamus vulputate, risus eget commodo eleifend, eros nibh porta quam, vitae lacinia leo libero at magna. Maecenas aliquam sagittis orci, et posuere nisi ultrices sit amet. Aliquam ex odio, malesuada sed posuere quis, pellentesque at mauris. Phasellus venenatis massa ex, eget pulvinar libero auctor pretium. Aliquam erat volutpat. Duis euismod justo in quam ullamcorper, in commodo massa vulputate.</div>
<br />
<br />
<div>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus pretium est a porttitor vehicula. Quisque vel commodo urna. Morbi mattis rutrum ante, id vehicula ex accumsan ut. Morbi viverra, eros vel porttitor facilisis, eros purus aliquet erat, nec lobortis felis elit pulvinar sem. Vivamus vulputate, risus eget commodo eleifend, eros nibh porta quam, vitae lacinia leo libero at magna. Maecenas aliquam sagittis orci, et posuere nisi ultrices sit amet. Aliquam ex odio, malesuada sed posuere quis, pellentesque at mauris. Phasellus venenatis massa ex, eget pulvinar libero auctor pretium. Aliquam erat volutpat. Duis euismod justo in quam ullamcorper, in commodo massa vulputate.</div>
<div class="pf-v6-c-pagination pf-m-plain pf-m-bottom">
  <div class="pf-v6-c-pagination__page-menu">
    <button
      class="pf-v6-c-menu-toggle pf-m-top pf-m-text pf-m-plain"
      type="button"
      aria-expanded="false"
      id="pagination-plain-bottom-menu-toggle"
    >
      <span class="pf-v6-c-menu-toggle__text">
        <b>1 - 10</b>&nbsp;of&nbsp;
        <b>36</b>
      </span>
      <span class="pf-v6-c-menu-toggle__controls">
        <span class="pf-v6-c-menu-toggle__toggle-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 20 20"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
            />
          </svg>
        </span>
      </span>
    </button>
  </div>
  <nav
    class="pf-v6-c-pagination__nav"
    aria-label="Pagination nav - plain bottom example"
  >
    <div class="pf-v6-c-pagination__nav-control pf-m-first">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Go to first page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 448 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M223.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L319.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L393.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34zm-192 34l136 136c9.4 9.4 24.6 9.4 33.9 0l22.6-22.6c9.4-9.4 9.4-24.6 0-33.9L127.9 256l96.4-96.4c9.4-9.4 9.4-24.6 0-33.9L201.7 103c-9.4-9.4-24.6-9.4-33.9 0l-136 136c-9.5 9.4-9.5 24.6-.1 34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-pagination__nav-control pf-m-prev">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Go to previous page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 256 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M31.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L127.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L201.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-pagination__nav-page-select">
      <span class="pf-v6-c-form-control">
        <input
          aria-label="Current page"
          type="number"
          min="1"
          max="4"
          value="1"
        />
      </span>
      <span aria-hidden="true">of 4</span>
    </div>
    <div class="pf-v6-c-pagination__nav-control pf-m-next">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Go to next page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 256 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-pagination__nav-control pf-m-last">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Go to last page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 448 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34zm192-34l-136-136c-9.4-9.4-24.6-9.4-33.9 0l-22.6 22.6c-9.4 9.4-9.4 24.6 0 33.9l96.4 96.4-96.4 96.4c-9.4 9.4-9.4 24.6 0 33.9l22.6 22.6c9.4 9.4 24.6 9.4 33.9 0l136-136c9.4-9.2 9.4-24.4 0-33.8z"
            />
          </svg>
        </span>
      </button>
    </div>
  </nav>
</div>

```

### Bottom sticky

```html
<div>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus pretium est a porttitor vehicula. Quisque vel commodo urna. Morbi mattis rutrum ante, id vehicula ex accumsan ut. Morbi viverra, eros vel porttitor facilisis, eros purus aliquet erat, nec lobortis felis elit pulvinar sem. Vivamus vulputate, risus eget commodo eleifend, eros nibh porta quam, vitae lacinia leo libero at magna. Maecenas aliquam sagittis orci, et posuere nisi ultrices sit amet. Aliquam ex odio, malesuada sed posuere quis, pellentesque at mauris. Phasellus venenatis massa ex, eget pulvinar libero auctor pretium. Aliquam erat volutpat. Duis euismod justo in quam ullamcorper, in commodo massa vulputate.</div>
<br />
<br />
<div>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus pretium est a porttitor vehicula. Quisque vel commodo urna. Morbi mattis rutrum ante, id vehicula ex accumsan ut. Morbi viverra, eros vel porttitor facilisis, eros purus aliquet erat, nec lobortis felis elit pulvinar sem. Vivamus vulputate, risus eget commodo eleifend, eros nibh porta quam, vitae lacinia leo libero at magna. Maecenas aliquam sagittis orci, et posuere nisi ultrices sit amet. Aliquam ex odio, malesuada sed posuere quis, pellentesque at mauris. Phasellus venenatis massa ex, eget pulvinar libero auctor pretium. Aliquam erat volutpat. Duis euismod justo in quam ullamcorper, in commodo massa vulputate.</div>
<br />
<br />
<div>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus pretium est a porttitor vehicula. Quisque vel commodo urna. Morbi mattis rutrum ante, id vehicula ex accumsan ut. Morbi viverra, eros vel porttitor facilisis, eros purus aliquet erat, nec lobortis felis elit pulvinar sem. Vivamus vulputate, risus eget commodo eleifend, eros nibh porta quam, vitae lacinia leo libero at magna. Maecenas aliquam sagittis orci, et posuere nisi ultrices sit amet. Aliquam ex odio, malesuada sed posuere quis, pellentesque at mauris. Phasellus venenatis massa ex, eget pulvinar libero auctor pretium. Aliquam erat volutpat. Duis euismod justo in quam ullamcorper, in commodo massa vulputate.</div>
<br />
<br />
<div>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus pretium est a porttitor vehicula. Quisque vel commodo urna. Morbi mattis rutrum ante, id vehicula ex accumsan ut. Morbi viverra, eros vel porttitor facilisis, eros purus aliquet erat, nec lobortis felis elit pulvinar sem. Vivamus vulputate, risus eget commodo eleifend, eros nibh porta quam, vitae lacinia leo libero at magna. Maecenas aliquam sagittis orci, et posuere nisi ultrices sit amet. Aliquam ex odio, malesuada sed posuere quis, pellentesque at mauris. Phasellus venenatis massa ex, eget pulvinar libero auctor pretium. Aliquam erat volutpat. Duis euismod justo in quam ullamcorper, in commodo massa vulputate.</div>
<div class="pf-v6-c-pagination pf-m-sticky pf-m-bottom">
  <div class="pf-v6-c-pagination__page-menu">
    <button
      class="pf-v6-c-menu-toggle pf-m-top pf-m-text pf-m-plain"
      type="button"
      aria-expanded="false"
      id="pagination-menu-toggle-bottom-sticky-example"
    >
      <span class="pf-v6-c-menu-toggle__text">
        <b>1 - 10</b>&nbsp;of&nbsp;
        <b>36</b>
      </span>
      <span class="pf-v6-c-menu-toggle__controls">
        <span class="pf-v6-c-menu-toggle__toggle-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 20 20"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
            />
          </svg>
        </span>
      </span>
    </button>
  </div>
  <nav
    class="pf-v6-c-pagination__nav"
    aria-label="Pagination nav - bottom sticky example"
  >
    <div class="pf-v6-c-pagination__nav-control pf-m-first">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Go to first page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 448 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M223.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L319.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L393.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34zm-192 34l136 136c9.4 9.4 24.6 9.4 33.9 0l22.6-22.6c9.4-9.4 9.4-24.6 0-33.9L127.9 256l96.4-96.4c9.4-9.4 9.4-24.6 0-33.9L201.7 103c-9.4-9.4-24.6-9.4-33.9 0l-136 136c-9.5 9.4-9.5 24.6-.1 34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-pagination__nav-control pf-m-prev">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Go to previous page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 256 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M31.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L127.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L201.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-pagination__nav-page-select">
      <span class="pf-v6-c-form-control">
        <input
          aria-label="Current page"
          type="number"
          min="1"
          max="4"
          value="1"
        />
      </span>
      <span aria-hidden="true">of 4</span>
    </div>
    <div class="pf-v6-c-pagination__nav-control pf-m-next">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Go to next page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 256 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-pagination__nav-control pf-m-last">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Go to last page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 448 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34zm192-34l-136-136c-9.4-9.4-24.6-9.4-33.9 0l-22.6 22.6c-9.4 9.4-9.4 24.6 0 33.9l96.4 96.4-96.4 96.4c-9.4 9.4-9.4 24.6 0 33.9l22.6 22.6c9.4 9.4 24.6 9.4 33.9 0l136-136c9.4-9.2 9.4-24.4 0-33.8z"
            />
          </svg>
        </span>
      </button>
    </div>
  </nav>
</div>

```

### Top sticky with base and stuck

This example shows the use of `.pf-m-sticky-base` and `.pf-m-sticky-stuck`. `.pf-m-sticky-stuck` can be applied dynamically as the page has scrolled to only show sticky styles when the pagination is "stuck" and floating above the content.

```html
<div class="pf-v6-c-pagination pf-m-sticky-stuck pf-m-sticky-base">
  <div class="pf-v6-c-pagination__total-items">
    <b>1 - 10</b>&nbsp;of&nbsp;
    <b>36</b>
  </div>
  <div class="pf-v6-c-pagination__page-menu">
    <button
      class="pf-v6-c-menu-toggle pf-m-text pf-m-plain"
      type="button"
      aria-expanded="false"
      id="pagination-top-sticky-base-stuck-menu-toggle"
    >
      <span class="pf-v6-c-menu-toggle__text">
        <b>1 - 10</b>&nbsp;of&nbsp;
        <b>36</b>
      </span>
      <span class="pf-v6-c-menu-toggle__controls">
        <span class="pf-v6-c-menu-toggle__toggle-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 20 20"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
            />
          </svg>
        </span>
      </span>
    </button>
  </div>
  <nav
    class="pf-v6-c-pagination__nav"
    aria-label="Pagination nav - top sticky with base and stuck example"
  >
    <div class="pf-v6-c-pagination__nav-control pf-m-first">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Go to first page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 448 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M223.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L319.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L393.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34zm-192 34l136 136c9.4 9.4 24.6 9.4 33.9 0l22.6-22.6c9.4-9.4 9.4-24.6 0-33.9L127.9 256l96.4-96.4c9.4-9.4 9.4-24.6 0-33.9L201.7 103c-9.4-9.4-24.6-9.4-33.9 0l-136 136c-9.5 9.4-9.5 24.6-.1 34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-pagination__nav-control pf-m-prev">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Go to previous page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 256 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M31.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L127.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L201.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-pagination__nav-page-select">
      <span class="pf-v6-c-form-control">
        <input
          aria-label="Current page"
          type="number"
          min="1"
          max="4"
          value="1"
        />
      </span>
      <span aria-hidden="true">of 4</span>
    </div>
    <div class="pf-v6-c-pagination__nav-control pf-m-next">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Go to next page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 256 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-pagination__nav-control pf-m-last">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Go to last page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 448 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34zm192-34l-136-136c-9.4-9.4-24.6-9.4-33.9 0l-22.6 22.6c-9.4 9.4-9.4 24.6 0 33.9l96.4 96.4-96.4 96.4c-9.4 9.4-9.4 24.6 0 33.9l22.6 22.6c9.4 9.4 24.6 9.4 33.9 0l136-136c9.4-9.2 9.4-24.4 0-33.8z"
            />
          </svg>
        </span>
      </button>
    </div>
  </nav>
</div>
<div>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus pretium est a porttitor vehicula. Quisque vel commodo urna. Morbi mattis rutrum ante, id vehicula ex accumsan ut. Morbi viverra, eros vel porttitor facilisis, eros purus aliquet erat, nec lobortis felis elit pulvinar sem. Vivamus vulputate, risus eget commodo eleifend, eros nibh porta quam, vitae lacinia leo libero at magna. Maecenas aliquam sagittis orci, et posuere nisi ultrices sit amet. Aliquam ex odio, malesuada sed posuere quis, pellentesque at mauris. Phasellus venenatis massa ex, eget pulvinar libero auctor pretium. Aliquam erat volutpat. Duis euismod justo in quam ullamcorper, in commodo massa vulputate.</div>
<br />
<br />
<div>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus pretium est a porttitor vehicula. Quisque vel commodo urna. Morbi mattis rutrum ante, id vehicula ex accumsan ut. Morbi viverra, eros vel porttitor facilisis, eros purus aliquet erat, nec lobortis felis elit pulvinar sem. Vivamus vulputate, risus eget commodo eleifend, eros nibh porta quam, vitae lacinia leo libero at magna. Maecenas aliquam sagittis orci, et posuere nisi ultrices sit amet. Aliquam ex odio, malesuada sed posuere quis, pellentesque at mauris. Phasellus venenatis massa ex, eget pulvinar libero auctor pretium. Aliquam erat volutpat. Duis euismod justo in quam ullamcorper, in commodo massa vulputate.</div>
<br />
<br />
<div>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus pretium est a porttitor vehicula. Quisque vel commodo urna. Morbi mattis rutrum ante, id vehicula ex accumsan ut. Morbi viverra, eros vel porttitor facilisis, eros purus aliquet erat, nec lobortis felis elit pulvinar sem. Vivamus vulputate, risus eget commodo eleifend, eros nibh porta quam, vitae lacinia leo libero at magna. Maecenas aliquam sagittis orci, et posuere nisi ultrices sit amet. Aliquam ex odio, malesuada sed posuere quis, pellentesque at mauris. Phasellus venenatis massa ex, eget pulvinar libero auctor pretium. Aliquam erat volutpat. Duis euismod justo in quam ullamcorper, in commodo massa vulputate.</div>
<br />
<br />
<div>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus pretium est a porttitor vehicula. Quisque vel commodo urna. Morbi mattis rutrum ante, id vehicula ex accumsan ut. Morbi viverra, eros vel porttitor facilisis, eros purus aliquet erat, nec lobortis felis elit pulvinar sem. Vivamus vulputate, risus eget commodo eleifend, eros nibh porta quam, vitae lacinia leo libero at magna. Maecenas aliquam sagittis orci, et posuere nisi ultrices sit amet. Aliquam ex odio, malesuada sed posuere quis, pellentesque at mauris. Phasellus venenatis massa ex, eget pulvinar libero auctor pretium. Aliquam erat volutpat. Duis euismod justo in quam ullamcorper, in commodo massa vulputate.</div>

```

### Bottom sticky with base and stuck

This example shows the use of `.pf-m-sticky-base` and `.pf-m-sticky-stuck` on bottom pagination. Like top pagination,`.pf-m-sticky-stuck` can be applied dynamically as the page has scrolled to only show sticky styles when the bottom pagination is "stuck" and floating above the content.

```html
<div>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus pretium est a porttitor vehicula. Quisque vel commodo urna. Morbi mattis rutrum ante, id vehicula ex accumsan ut. Morbi viverra, eros vel porttitor facilisis, eros purus aliquet erat, nec lobortis felis elit pulvinar sem. Vivamus vulputate, risus eget commodo eleifend, eros nibh porta quam, vitae lacinia leo libero at magna. Maecenas aliquam sagittis orci, et posuere nisi ultrices sit amet. Aliquam ex odio, malesuada sed posuere quis, pellentesque at mauris. Phasellus venenatis massa ex, eget pulvinar libero auctor pretium. Aliquam erat volutpat. Duis euismod justo in quam ullamcorper, in commodo massa vulputate.</div>
<br />
<br />
<div>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus pretium est a porttitor vehicula. Quisque vel commodo urna. Morbi mattis rutrum ante, id vehicula ex accumsan ut. Morbi viverra, eros vel porttitor facilisis, eros purus aliquet erat, nec lobortis felis elit pulvinar sem. Vivamus vulputate, risus eget commodo eleifend, eros nibh porta quam, vitae lacinia leo libero at magna. Maecenas aliquam sagittis orci, et posuere nisi ultrices sit amet. Aliquam ex odio, malesuada sed posuere quis, pellentesque at mauris. Phasellus venenatis massa ex, eget pulvinar libero auctor pretium. Aliquam erat volutpat. Duis euismod justo in quam ullamcorper, in commodo massa vulputate.</div>
<br />
<br />
<div>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus pretium est a porttitor vehicula. Quisque vel commodo urna. Morbi mattis rutrum ante, id vehicula ex accumsan ut. Morbi viverra, eros vel porttitor facilisis, eros purus aliquet erat, nec lobortis felis elit pulvinar sem. Vivamus vulputate, risus eget commodo eleifend, eros nibh porta quam, vitae lacinia leo libero at magna. Maecenas aliquam sagittis orci, et posuere nisi ultrices sit amet. Aliquam ex odio, malesuada sed posuere quis, pellentesque at mauris. Phasellus venenatis massa ex, eget pulvinar libero auctor pretium. Aliquam erat volutpat. Duis euismod justo in quam ullamcorper, in commodo massa vulputate.</div>
<br />
<br />
<div>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus pretium est a porttitor vehicula. Quisque vel commodo urna. Morbi mattis rutrum ante, id vehicula ex accumsan ut. Morbi viverra, eros vel porttitor facilisis, eros purus aliquet erat, nec lobortis felis elit pulvinar sem. Vivamus vulputate, risus eget commodo eleifend, eros nibh porta quam, vitae lacinia leo libero at magna. Maecenas aliquam sagittis orci, et posuere nisi ultrices sit amet. Aliquam ex odio, malesuada sed posuere quis, pellentesque at mauris. Phasellus venenatis massa ex, eget pulvinar libero auctor pretium. Aliquam erat volutpat. Duis euismod justo in quam ullamcorper, in commodo massa vulputate.</div>
<div class="pf-v6-c-pagination pf-m-sticky-stuck pf-m-sticky-base pf-m-bottom">
  <div class="pf-v6-c-pagination__page-menu">
    <button
      class="pf-v6-c-menu-toggle pf-m-top pf-m-text pf-m-plain"
      type="button"
      aria-expanded="false"
      id="pagination-bottom-sticky-base-stuck-menu-toggle"
    >
      <span class="pf-v6-c-menu-toggle__text">
        <b>1 - 10</b>&nbsp;of&nbsp;
        <b>36</b>
      </span>
      <span class="pf-v6-c-menu-toggle__controls">
        <span class="pf-v6-c-menu-toggle__toggle-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 20 20"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
            />
          </svg>
        </span>
      </span>
    </button>
  </div>
  <nav
    class="pf-v6-c-pagination__nav"
    aria-label="Pagination nav - bottom sticky with base and stuck example"
  >
    <div class="pf-v6-c-pagination__nav-control pf-m-first">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Go to first page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 448 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M223.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L319.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L393.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34zm-192 34l136 136c9.4 9.4 24.6 9.4 33.9 0l22.6-22.6c9.4-9.4 9.4-24.6 0-33.9L127.9 256l96.4-96.4c9.4-9.4 9.4-24.6 0-33.9L201.7 103c-9.4-9.4-24.6-9.4-33.9 0l-136 136c-9.5 9.4-9.5 24.6-.1 34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-pagination__nav-control pf-m-prev">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Go to previous page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 256 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M31.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L127.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L201.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-pagination__nav-page-select">
      <span class="pf-v6-c-form-control">
        <input
          aria-label="Current page"
          type="number"
          min="1"
          max="4"
          value="1"
        />
      </span>
      <span aria-hidden="true">of 4</span>
    </div>
    <div class="pf-v6-c-pagination__nav-control pf-m-next">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Go to next page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 256 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-pagination__nav-control pf-m-last">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Go to last page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 448 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34zm192-34l-136-136c-9.4-9.4-24.6-9.4-33.9 0l-22.6 22.6c-9.4 9.4-9.4 24.6 0 33.9l96.4 96.4-96.4 96.4c-9.4 9.4-9.4 24.6 0 33.9l22.6 22.6c9.4 9.4 24.6 9.4 33.9 0l136-136c9.4-9.2 9.4-24.4 0-33.8z"
            />
          </svg>
        </span>
      </button>
    </div>
  </nav>
</div>

```

### Bottom static

```html
<div>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus pretium est a porttitor vehicula. Quisque vel commodo urna. Morbi mattis rutrum ante, id vehicula ex accumsan ut. Morbi viverra, eros vel porttitor facilisis, eros purus aliquet erat, nec lobortis felis elit pulvinar sem. Vivamus vulputate, risus eget commodo eleifend, eros nibh porta quam, vitae lacinia leo libero at magna. Maecenas aliquam sagittis orci, et posuere nisi ultrices sit amet. Aliquam ex odio, malesuada sed posuere quis, pellentesque at mauris. Phasellus venenatis massa ex, eget pulvinar libero auctor pretium. Aliquam erat volutpat. Duis euismod justo in quam ullamcorper, in commodo massa vulputate.</div>
<br />
<br />
<div>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus pretium est a porttitor vehicula. Quisque vel commodo urna. Morbi mattis rutrum ante, id vehicula ex accumsan ut. Morbi viverra, eros vel porttitor facilisis, eros purus aliquet erat, nec lobortis felis elit pulvinar sem. Vivamus vulputate, risus eget commodo eleifend, eros nibh porta quam, vitae lacinia leo libero at magna. Maecenas aliquam sagittis orci, et posuere nisi ultrices sit amet. Aliquam ex odio, malesuada sed posuere quis, pellentesque at mauris. Phasellus venenatis massa ex, eget pulvinar libero auctor pretium. Aliquam erat volutpat. Duis euismod justo in quam ullamcorper, in commodo massa vulputate.</div>
<br />
<br />
<div>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus pretium est a porttitor vehicula. Quisque vel commodo urna. Morbi mattis rutrum ante, id vehicula ex accumsan ut. Morbi viverra, eros vel porttitor facilisis, eros purus aliquet erat, nec lobortis felis elit pulvinar sem. Vivamus vulputate, risus eget commodo eleifend, eros nibh porta quam, vitae lacinia leo libero at magna. Maecenas aliquam sagittis orci, et posuere nisi ultrices sit amet. Aliquam ex odio, malesuada sed posuere quis, pellentesque at mauris. Phasellus venenatis massa ex, eget pulvinar libero auctor pretium. Aliquam erat volutpat. Duis euismod justo in quam ullamcorper, in commodo massa vulputate.</div>
<br />
<br />
<div>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus pretium est a porttitor vehicula. Quisque vel commodo urna. Morbi mattis rutrum ante, id vehicula ex accumsan ut. Morbi viverra, eros vel porttitor facilisis, eros purus aliquet erat, nec lobortis felis elit pulvinar sem. Vivamus vulputate, risus eget commodo eleifend, eros nibh porta quam, vitae lacinia leo libero at magna. Maecenas aliquam sagittis orci, et posuere nisi ultrices sit amet. Aliquam ex odio, malesuada sed posuere quis, pellentesque at mauris. Phasellus venenatis massa ex, eget pulvinar libero auctor pretium. Aliquam erat volutpat. Duis euismod justo in quam ullamcorper, in commodo massa vulputate.</div>
<div class="pf-v6-c-pagination pf-m-static pf-m-bottom">
  <div class="pf-v6-c-pagination__page-menu">
    <button
      class="pf-v6-c-menu-toggle pf-m-top pf-m-text pf-m-plain"
      type="button"
      aria-expanded="false"
      id="pagination-menu-toggle-bottom-sticky-example"
    >
      <span class="pf-v6-c-menu-toggle__text">
        <b>1 - 10</b>&nbsp;of&nbsp;
        <b>36</b>
      </span>
      <span class="pf-v6-c-menu-toggle__controls">
        <span class="pf-v6-c-menu-toggle__toggle-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 20 20"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
            />
          </svg>
        </span>
      </span>
    </button>
  </div>
  <nav
    class="pf-v6-c-pagination__nav"
    aria-label="Pagination nav - bottom sticky example"
  >
    <div class="pf-v6-c-pagination__nav-control pf-m-first">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Go to first page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 448 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M223.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L319.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L393.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34zm-192 34l136 136c9.4 9.4 24.6 9.4 33.9 0l22.6-22.6c9.4-9.4 9.4-24.6 0-33.9L127.9 256l96.4-96.4c9.4-9.4 9.4-24.6 0-33.9L201.7 103c-9.4-9.4-24.6-9.4-33.9 0l-136 136c-9.5 9.4-9.5 24.6-.1 34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-pagination__nav-control pf-m-prev">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Go to previous page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 256 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M31.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L127.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L201.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-pagination__nav-page-select">
      <span class="pf-v6-c-form-control">
        <input
          aria-label="Current page"
          type="number"
          min="1"
          max="4"
          value="1"
        />
      </span>
      <span aria-hidden="true">of 4</span>
    </div>
    <div class="pf-v6-c-pagination__nav-control pf-m-next">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Go to next page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 256 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-pagination__nav-control pf-m-last">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Go to last page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 448 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34zm192-34l-136-136c-9.4-9.4-24.6-9.4-33.9 0l-22.6 22.6c-9.4 9.4-9.4 24.6 0 33.9l96.4 96.4-96.4 96.4c-9.4 9.4-9.4 24.6 0 33.9l22.6 22.6c9.4 9.4 24.6 9.4 33.9 0l136-136c9.4-9.2 9.4-24.4 0-33.8z"
            />
          </svg>
        </span>
      </button>
    </div>
  </nav>
</div>

```

### Top disabled

```html
<div class="pf-v6-c-pagination">
  <div class="pf-v6-c-pagination__total-items">
    <b>1 - 10</b>&nbsp;of&nbsp;
    <b>36</b>
  </div>
  <div class="pf-v6-c-pagination__page-menu">
    <button
      class="pf-v6-c-menu-toggle pf-m-text pf-m-plain pf-m-disabled"
      type="button"
      aria-expanded="false"
      disabled
      id="pagination-menu-toggle-top-disabled-example"
    >
      <span class="pf-v6-c-menu-toggle__text">
        <b>1 - 10</b>&nbsp;of&nbsp;
        <b>36</b>
      </span>
      <span class="pf-v6-c-menu-toggle__controls">
        <span class="pf-v6-c-menu-toggle__toggle-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 20 20"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
            />
          </svg>
        </span>
      </span>
    </button>
  </div>
  <nav
    class="pf-v6-c-pagination__nav"
    aria-label="Pagination nav - top disabled example"
  >
    <div class="pf-v6-c-pagination__nav-control pf-m-first">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Go to first page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 448 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M223.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L319.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L393.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34zm-192 34l136 136c9.4 9.4 24.6 9.4 33.9 0l22.6-22.6c9.4-9.4 9.4-24.6 0-33.9L127.9 256l96.4-96.4c9.4-9.4 9.4-24.6 0-33.9L201.7 103c-9.4-9.4-24.6-9.4-33.9 0l-136 136c-9.5 9.4-9.5 24.6-.1 34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-pagination__nav-control pf-m-prev">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Go to previous page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 256 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M31.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L127.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L201.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-pagination__nav-page-select">
      <span class="pf-v6-c-form-control pf-m-disabled">
        <input
          disabled
          aria-label="Current page"
          type="number"
          min="1"
          max="4"
          value="1"
        />
      </span>
      <span aria-hidden="true">of 4</span>
    </div>
    <div class="pf-v6-c-pagination__nav-control pf-m-next">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Go to next page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 256 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-pagination__nav-control pf-m-last">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Go to last page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 448 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34zm192-34l-136-136c-9.4-9.4-24.6-9.4-33.9 0l-22.6 22.6c-9.4 9.4-9.4 24.6 0 33.9l96.4 96.4-96.4 96.4c-9.4 9.4-9.4 24.6 0 33.9l22.6 22.6c9.4 9.4 24.6 9.4 33.9 0l136-136c9.4-9.2 9.4-24.4 0-33.8z"
            />
          </svg>
        </span>
      </button>
    </div>
  </nav>
</div>

```

### Compact

```html
<div class="pf-v6-c-pagination pf-m-compact">
  <div class="pf-v6-c-pagination__total-items">
    <b>1 - 10</b>&nbsp;of&nbsp;
    <b>36</b>
  </div>
  <div class="pf-v6-c-pagination__page-menu">
    <button
      class="pf-v6-c-menu-toggle pf-m-text pf-m-plain"
      type="button"
      aria-expanded="false"
      id="pagination-menu-toggle-compact-example"
    >
      <span class="pf-v6-c-menu-toggle__text">
        <b>1 - 10</b>&nbsp;of&nbsp;
        <b>36</b>
      </span>
      <span class="pf-v6-c-menu-toggle__controls">
        <span class="pf-v6-c-menu-toggle__toggle-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 20 20"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
            />
          </svg>
        </span>
      </span>
    </button>
  </div>
  <nav
    class="pf-v6-c-pagination__nav"
    aria-label="Pagination nav - compact example"
  >
    <div class="pf-v6-c-pagination__nav-control pf-m-prev">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Go to previous page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 256 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M31.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L127.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L201.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-pagination__nav-control pf-m-next">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Go to next page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 256 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34z"
            />
          </svg>
        </span>
      </button>
    </div>
  </nav>
</div>

```

### Top with display summary modifier

```html
<div class="pf-v6-c-pagination pf-m-display-summary">
  <div class="pf-v6-c-pagination__total-items">
    <b>1 - 10</b>&nbsp;of&nbsp;
    <b>36</b>
  </div>
  <div class="pf-v6-c-pagination__page-menu">
    <button
      class="pf-v6-c-menu-toggle pf-m-text pf-m-plain"
      type="button"
      aria-expanded="false"
      id="pagination-top-with-summary-modifier-menu-toggle"
    >
      <span class="pf-v6-c-menu-toggle__text">
        <b>1 - 10</b>&nbsp;of&nbsp;
        <b>36</b>
      </span>
      <span class="pf-v6-c-menu-toggle__controls">
        <span class="pf-v6-c-menu-toggle__toggle-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 20 20"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
            />
          </svg>
        </span>
      </span>
    </button>
  </div>
  <nav
    class="pf-v6-c-pagination__nav"
    aria-label="Pagination nav - top with display summary modifier example"
  >
    <div class="pf-v6-c-pagination__nav-control pf-m-first">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Go to first page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 448 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M223.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L319.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L393.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34zm-192 34l136 136c9.4 9.4 24.6 9.4 33.9 0l22.6-22.6c9.4-9.4 9.4-24.6 0-33.9L127.9 256l96.4-96.4c9.4-9.4 9.4-24.6 0-33.9L201.7 103c-9.4-9.4-24.6-9.4-33.9 0l-136 136c-9.5 9.4-9.5 24.6-.1 34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-pagination__nav-control pf-m-prev">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Go to previous page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 256 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M31.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L127.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L201.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-pagination__nav-page-select">
      <span class="pf-v6-c-form-control">
        <input
          aria-label="Current page"
          type="number"
          min="1"
          max="4"
          value="1"
        />
      </span>
      <span aria-hidden="true">of 4</span>
    </div>
    <div class="pf-v6-c-pagination__nav-control pf-m-next">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Go to next page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 256 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-pagination__nav-control pf-m-last">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Go to last page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 448 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34zm192-34l-136-136c-9.4-9.4-24.6-9.4-33.9 0l-22.6 22.6c-9.4 9.4-9.4 24.6 0 33.9l96.4 96.4-96.4 96.4c-9.4 9.4-9.4 24.6 0 33.9l22.6 22.6c9.4 9.4 24.6 9.4 33.9 0l136-136c9.4-9.2 9.4-24.4 0-33.8z"
            />
          </svg>
        </span>
      </button>
    </div>
  </nav>
</div>

```

### Top with display full modifier

```html
<div class="pf-v6-c-pagination pf-m-display-full">
  <div class="pf-v6-c-pagination__total-items">
    <b>1 - 10</b>&nbsp;of&nbsp;
    <b>36</b>
  </div>
  <div class="pf-v6-c-pagination__page-menu">
    <button
      class="pf-v6-c-menu-toggle pf-m-text pf-m-plain"
      type="button"
      aria-expanded="false"
      id="pagination-top-with-full-modifier-menu-toggle"
    >
      <span class="pf-v6-c-menu-toggle__text">
        <b>1 - 10</b>&nbsp;of&nbsp;
        <b>36</b>
      </span>
      <span class="pf-v6-c-menu-toggle__controls">
        <span class="pf-v6-c-menu-toggle__toggle-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 20 20"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
            />
          </svg>
        </span>
      </span>
    </button>
  </div>
  <nav
    class="pf-v6-c-pagination__nav"
    aria-label="Pagination nav - top with display full modifier example"
  >
    <div class="pf-v6-c-pagination__nav-control pf-m-first">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Go to first page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 448 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M223.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L319.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L393.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34zm-192 34l136 136c9.4 9.4 24.6 9.4 33.9 0l22.6-22.6c9.4-9.4 9.4-24.6 0-33.9L127.9 256l96.4-96.4c9.4-9.4 9.4-24.6 0-33.9L201.7 103c-9.4-9.4-24.6-9.4-33.9 0l-136 136c-9.5 9.4-9.5 24.6-.1 34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-pagination__nav-control pf-m-prev">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Go to previous page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 256 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M31.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L127.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L201.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-pagination__nav-page-select">
      <span class="pf-v6-c-form-control">
        <input
          aria-label="Current page"
          type="number"
          min="1"
          max="4"
          value="1"
        />
      </span>
      <span aria-hidden="true">of 4</span>
    </div>
    <div class="pf-v6-c-pagination__nav-control pf-m-next">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Go to next page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 256 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-pagination__nav-control pf-m-last">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Go to last page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 448 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34zm192-34l-136-136c-9.4-9.4-24.6-9.4-33.9 0l-22.6 22.6c-9.4 9.4-9.4 24.6 0 33.9l96.4 96.4-96.4 96.4c-9.4 9.4-9.4 24.6 0 33.9l22.6 22.6c9.4 9.4 24.6 9.4 33.9 0l136-136c9.4-9.2 9.4-24.4 0-33.8z"
            />
          </svg>
        </span>
      </button>
    </div>
  </nav>
</div>

```

### Top with responsive display summary and display full modifiers

```html
<div
  class="pf-v6-c-pagination pf-m-display-summary pf-m-display-full-on-lg pf-m-display-summary-on-xl pf-m-display-full-on-2xl"
>
  <div class="pf-v6-c-pagination__total-items">
    <b>1 - 10</b>&nbsp;of&nbsp;
    <b>36</b>
  </div>
  <div class="pf-v6-c-pagination__page-menu">
    <button
      class="pf-v6-c-menu-toggle pf-m-text pf-m-plain"
      type="button"
      aria-expanded="false"
      id="pagination-top-with-responsive-summary-navigation-modifiers-menu-toggle"
    >
      <span class="pf-v6-c-menu-toggle__text">
        <b>1 - 10</b>&nbsp;of&nbsp;
        <b>36</b>
      </span>
      <span class="pf-v6-c-menu-toggle__controls">
        <span class="pf-v6-c-menu-toggle__toggle-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 20 20"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
            />
          </svg>
        </span>
      </span>
    </button>
  </div>
  <nav
    class="pf-v6-c-pagination__nav"
    aria-label="Pagination nav - top with responsive display summary and display full modifiers example"
  >
    <div class="pf-v6-c-pagination__nav-control pf-m-first">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Go to first page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 448 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M223.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L319.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L393.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34zm-192 34l136 136c9.4 9.4 24.6 9.4 33.9 0l22.6-22.6c9.4-9.4 9.4-24.6 0-33.9L127.9 256l96.4-96.4c9.4-9.4 9.4-24.6 0-33.9L201.7 103c-9.4-9.4-24.6-9.4-33.9 0l-136 136c-9.5 9.4-9.5 24.6-.1 34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-pagination__nav-control pf-m-prev">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Go to previous page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 256 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M31.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L127.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L201.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-pagination__nav-page-select">
      <span class="pf-v6-c-form-control">
        <input
          aria-label="Current page"
          type="number"
          min="1"
          max="4"
          value="1"
        />
      </span>
      <span aria-hidden="true">of 4</span>
    </div>
    <div class="pf-v6-c-pagination__nav-control pf-m-next">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Go to next page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 256 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-pagination__nav-control pf-m-last">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Go to last page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 448 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34zm192-34l-136-136c-9.4-9.4-24.6-9.4-33.9 0l-22.6 22.6c-9.4 9.4-9.4 24.6 0 33.9l96.4 96.4-96.4 96.4c-9.4 9.4-9.4 24.6 0 33.9l22.6 22.6c9.4 9.4 24.6 9.4 33.9 0l136-136c9.4-9.2 9.4-24.4 0-33.8z"
            />
          </svg>
        </span>
      </button>
    </div>
  </nav>
</div>

```

### Compact display full modifier

```html
<div class="pf-v6-c-pagination pf-m-display-full pf-m-compact">
  <div class="pf-v6-c-pagination__total-items">
    <b>1 - 10</b>&nbsp;of&nbsp;
    <b>36</b>
  </div>
  <div class="pf-v6-c-pagination__page-menu">
    <button
      class="pf-v6-c-menu-toggle pf-m-text pf-m-plain"
      type="button"
      aria-expanded="false"
      id="pagination-compact-with-full-modifier-menu-toggle"
    >
      <span class="pf-v6-c-menu-toggle__text">
        <b>1 - 10</b>&nbsp;of&nbsp;
        <b>36</b>
      </span>
      <span class="pf-v6-c-menu-toggle__controls">
        <span class="pf-v6-c-menu-toggle__toggle-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 20 20"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
            />
          </svg>
        </span>
      </span>
    </button>
  </div>
  <nav
    class="pf-v6-c-pagination__nav"
    aria-label="Pagination nav - compact display full modifier example"
  >
    <div class="pf-v6-c-pagination__nav-control pf-m-prev">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Go to previous page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 256 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M31.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L127.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L201.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-pagination__nav-control pf-m-next">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Go to next page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 256 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34z"
            />
          </svg>
        </span>
      </button>
    </div>
  </nav>
</div>

```

### Inset

```html
<div
  class="pf-v6-c-pagination pf-m-inset-none pf-m-inset-md-on-md pf-m-inset-2xl-on-lg"
>
  <div class="pf-v6-c-pagination__total-items">
    <b>1 - 10</b>&nbsp;of&nbsp;
    <b>36</b>
  </div>
  <div class="pf-v6-c-pagination__page-menu">
    <button
      class="pf-v6-c-menu-toggle pf-m-text pf-m-plain"
      type="button"
      aria-expanded="false"
      id="pagination-inset-menu-toggle"
    >
      <span class="pf-v6-c-menu-toggle__text">
        <b>1 - 10</b>&nbsp;of&nbsp;
        <b>36</b>
      </span>
      <span class="pf-v6-c-menu-toggle__controls">
        <span class="pf-v6-c-menu-toggle__toggle-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 20 20"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
            />
          </svg>
        </span>
      </span>
    </button>
  </div>
  <nav
    class="pf-v6-c-pagination__nav"
    aria-label="Pagination nav - inset example"
  >
    <div class="pf-v6-c-pagination__nav-control pf-m-first">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Go to first page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 448 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M223.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L319.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L393.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34zm-192 34l136 136c9.4 9.4 24.6 9.4 33.9 0l22.6-22.6c9.4-9.4 9.4-24.6 0-33.9L127.9 256l96.4-96.4c9.4-9.4 9.4-24.6 0-33.9L201.7 103c-9.4-9.4-24.6-9.4-33.9 0l-136 136c-9.5 9.4-9.5 24.6-.1 34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-pagination__nav-control pf-m-prev">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Go to previous page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 256 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M31.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L127.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L201.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-pagination__nav-page-select">
      <span class="pf-v6-c-form-control">
        <input
          aria-label="Current page"
          type="number"
          min="1"
          max="4"
          value="1"
        />
      </span>
      <span aria-hidden="true">of 4</span>
    </div>
    <div class="pf-v6-c-pagination__nav-control pf-m-next">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Go to next page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 256 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-pagination__nav-control pf-m-last">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Go to last page"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 448 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34zm192-34l-136-136c-9.4-9.4-24.6-9.4-33.9 0l-22.6 22.6c-9.4 9.4-9.4 24.6 0 33.9l96.4 96.4-96.4 96.4c-9.4 9.4-9.4 24.6 0 33.9l22.6 22.6c9.4 9.4 24.6 9.4 33.9 0l136-136c9.4-9.2 9.4-24.4 0-33.8z"
            />
          </svg>
        </span>
      </button>
    </div>
  </nav>
</div>

```

## Documentation

### Accessibility

| Attribute | Applied to | Outcome |
| -- | -- | -- |
| `aria-label`  | `.pf-v6-c-pagination__nav` |  Provides an accessible name for pagination navigation element. **Required** |
| `type="number"` | `.pf-v6-c-pagination__nav-page-select` > `.pf-v6-c-form-control` | Defines a field as a number. **Required** |
| `value` | `.pf-v6-c-pagination__nav-page-select` > `.pf-v6-c-form-control` | Provides initial integer value. **Required** |
| `min` | `.pf-v6-c-pagination__nav-page-select` > `.pf-v6-c-form-control` | Provides minimum integer value. **Required** |
| `max` | `.pf-v6-c-pagination__nav-page-select` > `.pf-v6-c-form-control` | Provides max integer value. **Required** |

### Usage

| Class | Applied to | Outcome |
| -- | -- | -- |
| `.pf-v6-c-pagination` | `<div>` |  Initiates pagination. |
| `.pf-v6-c-pagination__current` | `<div>` |  Initiates element to display currently displayed items for use in responsive view. Only needed for default pagination, not `.pf-m-bottom`. |
| `.pf-v6-c-pagination__total-items` | `<div>` | Initiates element to replace the menu toggle on summary. |
| `.pf-v6-c-pagination__page-menu` | `<div>` | Initiates wrapper element for the pagination menu toggle. **Required** when a menu toggle is intended or expected to be rendered. |
| `.pf-v6-c-pagination__nav` | `<nav>` |  Initiates pagination nav. |
| `.pf-v6-c-pagination__nav-control` | `<div>` |  Initiates pagination nav control. |
| `.pf-v6-c-pagination__nav-page-select` | `<div>` |  Initiates pagination nav page select. |
| `.pf-m-display-summary{-on-[breakpoint]}` | `.pf-v6-c-pagination` | Modifies for summary display pagination component styles at optional [breakpoint](/foundations-and-styles/design-tokens/all-design-tokens). |
| `.pf-m-display-full{-on-[breakpoint]}` | `.pf-v6-c-pagination` | Modifies for full display pagination component styles at optional [breakpoint](/foundations-and-styles/design-tokens/all-design-tokens). |
| `.pf-m-bottom` | `.pf-v6-c-pagination` | Modifies for bottom pagination component styles. |
| `.pf-m-compact` | `.pf-v6-c-pagination` | Modifies for compact pagination component styles. |
| `.pf-m-static` | `.pf-v6-c-pagination.pf-m-bottom` | Modifies bottom pagination to not be positioned sticky on summary. |
| `.pf-m-sticky` | `.pf-v6-c-pagination` | Modifies the pagination to be sticky to its container. It will be sticky to the top of the container by default, and sticky to the bottom of the container when applied to `.pf-v6-c-pagination.pf-m-bottom`. |
| `.pf-m-sticky-base` | `.pf-v6-c-pagination` | Makes the pagination sticky on scroll, but does not apply sticky styling. `.pf-m-sticky-stuck` must be used to apply sticky styling.  |
| `.pf-m-sticky-stuck` | `.pf-v6-c-pagination.pf-m-sticky-base` | Applies sticky styling to a pagination with `.pf-m-sticky-base`. |
| `.pf-m-plain` | `.pf-v6-c-pagination.pf-m-bottom` | Modifies the pagination to have a transparent background. Only applies outside of glass theme. |
| `.pf-m-no-plain-on-glass` | `.pf-v6-c-pagination.pf-m-bottom` | Prevents the pagination from being transparent on glass theme. |
| `.pf-m-inset-{none, sm, md, lg, xl, 2xl}{-on-[breakpoint]}` | `.pf-v6-c-pagination` | Modifies pagination horizontal padding at optional [breakpoint](/foundations-and-styles/design-tokens/all-design-tokens). |
| `.pf-m-page-insets` | `.pf-v6-c-pagination` |  Modifies the pagination component padding/inset to visually match padding of page elements. |
| `.pf-m-first` | `.pf-v6-c-pagination__nav-control` | Indicates the control is for the first page button. |
| `.pf-m-prev` | `.pf-v6-c-pagination__nav-control` | Indicates the control is for the previous page button. |
| `.pf-m-next` | `.pf-v6-c-pagination__nav-control` | Indicates the control is for the next page button. |
| `.pf-m-last` | `.pf-v6-c-pagination__nav-control` | Indicates the control is for the last page button. |
