---
id: Toggle group
section: components
cssPrefix: pf-v6-c-toggle-group
---## Examples

### Default

```html
<div class="pf-v6-c-toggle-group">
  <div class="pf-v6-c-toggle-group__item">
    <button class="pf-v6-c-toggle-group__button" type="button">
      <span class="pf-v6-c-toggle-group__text">Option 1</span>
    </button>
  </div>
  <div class="pf-v6-c-toggle-group__item">
    <button class="pf-v6-c-toggle-group__button" type="button">
      <span class="pf-v6-c-toggle-group__text">Option 2</span>
    </button>
  </div>
  <div class="pf-v6-c-toggle-group__item">
    <button class="pf-v6-c-toggle-group__button" type="button">
      <span class="pf-v6-c-toggle-group__text">Option 3</span>
    </button>
  </div>
</div>

<br />

<div class="pf-v6-c-toggle-group">
  <div class="pf-v6-c-toggle-group__item">
    <button class="pf-v6-c-toggle-group__button pf-m-selected" type="button">
      <span class="pf-v6-c-toggle-group__text">Option 1</span>
    </button>
  </div>
  <div class="pf-v6-c-toggle-group__item">
    <button class="pf-v6-c-toggle-group__button pf-m-selected" type="button">
      <span class="pf-v6-c-toggle-group__text">Option 2</span>
    </button>
  </div>
  <div class="pf-v6-c-toggle-group__item">
    <button class="pf-v6-c-toggle-group__button" type="button">
      <span class="pf-v6-c-toggle-group__text">Option 3</span>
    </button>
  </div>
</div>

<br />

<div class="pf-v6-c-toggle-group">
  <div class="pf-v6-c-toggle-group__item">
    <button class="pf-v6-c-toggle-group__button" type="button">
      <span class="pf-v6-c-toggle-group__text">Option 1</span>
    </button>
  </div>
  <div class="pf-v6-c-toggle-group__item">
    <button class="pf-v6-c-toggle-group__button" type="button">
      <span class="pf-v6-c-toggle-group__text">Option 2</span>
    </button>
  </div>
  <div class="pf-v6-c-toggle-group__item">
    <button class="pf-v6-c-toggle-group__button" type="button" disabled>
      <span class="pf-v6-c-toggle-group__text">Option 3</span>
    </button>
  </div>
</div>

```

### With icon

```html
<div class="pf-v6-c-toggle-group">
  <div class="pf-v6-c-toggle-group__item">
    <button
      class="pf-v6-c-toggle-group__button"
      type="button"
      aria-label="Copy button"
    >
      <span class="pf-v6-c-toggle-group__icon">
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
            d="M28 7v22.607c0 .768-.622 1.393-1.387 1.393H10a1 1 0 1 1 0-2h16V7a1 1 0 1 1 2 0Zm-6.5 19h-16c-.827 0-1.5-.673-1.5-1.5V8a1.001 1.001 0 0 1 .294-.708l5.998-5.998A1.001 1.001 0 0 1 11 1h10.5c.827 0 1.5.673 1.5 1.5v22c0 .827-.673 1.5-1.5 1.5ZM7.414 7H10V4.414L7.414 7ZM21 3h-9v4.614C12 8.378 11.378 9 10.613 9H6v15h15V3Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <div class="pf-v6-c-toggle-group__item">
    <button
      class="pf-v6-c-toggle-group__button"
      type="button"
      aria-label="Undo button"
    >
      <span class="pf-v6-c-toggle-group__icon">
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
            d="M31 20c0 5.514-4.486 10-10 10H6a1 1 0 1 1 0-2h15c4.411 0 8-3.589 8-8s-3.589-8-8-8H4.414l6.293 6.293a.999.999 0 1 1-1.414 1.414l-7.647-7.646c-.283-.283-.439-.66-.439-1.061s.156-.777.439-1.061l7.646-7.646a.999.999 0 1 1 1.414 1.414L4.413 10h16.586c5.514 0 10 4.486 10 10Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <div class="pf-v6-c-toggle-group__item">
    <button
      class="pf-v6-c-toggle-group__button"
      type="button"
      aria-label="Share button"
    >
      <span class="pf-v6-c-toggle-group__icon">
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
            d="M9.293 8.707a.999.999 0 0 1 0-1.414l5.646-5.647a1.501 1.501 0 0 1 2.121 0l5.646 5.646a.999.999 0 1 1-1.414 1.414l-4.293-4.293v18.586a1 1 0 1 1-2 0V4.414l-4.293 4.293a.999.999 0 0 1-1.414 0ZM24.5 14H22a1 1 0 1 0 0 2h2v13H8V16h2a1 1 0 1 0 0-2H7.5c-.827 0-1.5.673-1.5 1.5v14c0 .827.673 1.5 1.5 1.5h17c.827 0 1.5-.673 1.5-1.5v-14c0-.827-.673-1.5-1.5-1.5Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

<br />

<div class="pf-v6-c-toggle-group">
  <div class="pf-v6-c-toggle-group__item">
    <button
      class="pf-v6-c-toggle-group__button pf-m-selected"
      type="button"
      aria-label="Copy button"
    >
      <span class="pf-v6-c-toggle-group__icon">
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
            d="M28 7v22.607c0 .768-.622 1.393-1.387 1.393H10a1 1 0 1 1 0-2h16V7a1 1 0 1 1 2 0Zm-6.5 19h-16c-.827 0-1.5-.673-1.5-1.5V8a1.001 1.001 0 0 1 .294-.708l5.998-5.998A1.001 1.001 0 0 1 11 1h10.5c.827 0 1.5.673 1.5 1.5v22c0 .827-.673 1.5-1.5 1.5ZM7.414 7H10V4.414L7.414 7ZM21 3h-9v4.614C12 8.378 11.378 9 10.613 9H6v15h15V3Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <div class="pf-v6-c-toggle-group__item">
    <button
      class="pf-v6-c-toggle-group__button"
      type="button"
      aria-label="Undo button"
    >
      <span class="pf-v6-c-toggle-group__icon">
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
            d="M31 20c0 5.514-4.486 10-10 10H6a1 1 0 1 1 0-2h15c4.411 0 8-3.589 8-8s-3.589-8-8-8H4.414l6.293 6.293a.999.999 0 1 1-1.414 1.414l-7.647-7.646c-.283-.283-.439-.66-.439-1.061s.156-.777.439-1.061l7.646-7.646a.999.999 0 1 1 1.414 1.414L4.413 10h16.586c5.514 0 10 4.486 10 10Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <div class="pf-v6-c-toggle-group__item">
    <button
      class="pf-v6-c-toggle-group__button"
      type="button"
      aria-label="Share button"
    >
      <span class="pf-v6-c-toggle-group__icon">
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
            d="M9.293 8.707a.999.999 0 0 1 0-1.414l5.646-5.647a1.501 1.501 0 0 1 2.121 0l5.646 5.646a.999.999 0 1 1-1.414 1.414l-4.293-4.293v18.586a1 1 0 1 1-2 0V4.414l-4.293 4.293a.999.999 0 0 1-1.414 0ZM24.5 14H22a1 1 0 1 0 0 2h2v13H8V16h2a1 1 0 1 0 0-2H7.5c-.827 0-1.5.673-1.5 1.5v14c0 .827.673 1.5 1.5 1.5h17c.827 0 1.5-.673 1.5-1.5v-14c0-.827-.673-1.5-1.5-1.5Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

<br />

<div class="pf-v6-c-toggle-group">
  <div class="pf-v6-c-toggle-group__item">
    <button
      class="pf-v6-c-toggle-group__button"
      type="button"
      aria-label="Copy button"
    >
      <span class="pf-v6-c-toggle-group__icon">
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
            d="M28 7v22.607c0 .768-.622 1.393-1.387 1.393H10a1 1 0 1 1 0-2h16V7a1 1 0 1 1 2 0Zm-6.5 19h-16c-.827 0-1.5-.673-1.5-1.5V8a1.001 1.001 0 0 1 .294-.708l5.998-5.998A1.001 1.001 0 0 1 11 1h10.5c.827 0 1.5.673 1.5 1.5v22c0 .827-.673 1.5-1.5 1.5ZM7.414 7H10V4.414L7.414 7ZM21 3h-9v4.614C12 8.378 11.378 9 10.613 9H6v15h15V3Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <div class="pf-v6-c-toggle-group__item">
    <button
      class="pf-v6-c-toggle-group__button"
      type="button"
      aria-label="Undo button"
    >
      <span class="pf-v6-c-toggle-group__icon">
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
            d="M31 20c0 5.514-4.486 10-10 10H6a1 1 0 1 1 0-2h15c4.411 0 8-3.589 8-8s-3.589-8-8-8H4.414l6.293 6.293a.999.999 0 1 1-1.414 1.414l-7.647-7.646c-.283-.283-.439-.66-.439-1.061s.156-.777.439-1.061l7.646-7.646a.999.999 0 1 1 1.414 1.414L4.413 10h16.586c5.514 0 10 4.486 10 10Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <div class="pf-v6-c-toggle-group__item">
    <button
      class="pf-v6-c-toggle-group__button"
      type="button"
      aria-label="Share button"
      disabled
    >
      <span class="pf-v6-c-toggle-group__icon">
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
            d="M9.293 8.707a.999.999 0 0 1 0-1.414l5.646-5.647a1.501 1.501 0 0 1 2.121 0l5.646 5.646a.999.999 0 1 1-1.414 1.414l-4.293-4.293v18.586a1 1 0 1 1-2 0V4.414l-4.293 4.293a.999.999 0 0 1-1.414 0ZM24.5 14H22a1 1 0 1 0 0 2h2v13H8V16h2a1 1 0 1 0 0-2H7.5c-.827 0-1.5.673-1.5 1.5v14c0 .827.673 1.5 1.5 1.5h17c.827 0 1.5-.673 1.5-1.5v-14c0-.827-.673-1.5-1.5-1.5Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

```

### Icon-and-text

```html
<div class="pf-v6-c-toggle-group">
  <div class="pf-v6-c-toggle-group__item">
    <button class="pf-v6-c-toggle-group__button" type="button">
      <span class="pf-v6-c-toggle-group__icon">
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
            d="M28 7v22.607c0 .768-.622 1.393-1.387 1.393H10a1 1 0 1 1 0-2h16V7a1 1 0 1 1 2 0Zm-6.5 19h-16c-.827 0-1.5-.673-1.5-1.5V8a1.001 1.001 0 0 1 .294-.708l5.998-5.998A1.001 1.001 0 0 1 11 1h10.5c.827 0 1.5.673 1.5 1.5v22c0 .827-.673 1.5-1.5 1.5ZM7.414 7H10V4.414L7.414 7ZM21 3h-9v4.614C12 8.378 11.378 9 10.613 9H6v15h15V3Z"
          />
        </svg>
      </span>
      <span class="pf-v6-c-toggle-group__text">Copy</span>
    </button>
  </div>
  <div class="pf-v6-c-toggle-group__item">
    <button
      class="pf-v6-c-toggle-group__button"
      type="button"
      aria-label="Undo button"
    >
      <span class="pf-v6-c-toggle-group__icon">
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
            d="M31 20c0 5.514-4.486 10-10 10H6a1 1 0 1 1 0-2h15c4.411 0 8-3.589 8-8s-3.589-8-8-8H4.414l6.293 6.293a.999.999 0 1 1-1.414 1.414l-7.647-7.646c-.283-.283-.439-.66-.439-1.061s.156-.777.439-1.061l7.646-7.646a.999.999 0 1 1 1.414 1.414L4.413 10h16.586c5.514 0 10 4.486 10 10Z"
          />
        </svg>
      </span>
      <span class="pf-v6-c-toggle-group__text">Undo</span>
    </button>
  </div>
  <div class="pf-v6-c-toggle-group__item">
    <button class="pf-v6-c-toggle-group__button pf-m-selected" type="button">
      <span class="pf-v6-c-toggle-group__icon">
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
            d="M9.293 8.707a.999.999 0 0 1 0-1.414l5.646-5.647a1.501 1.501 0 0 1 2.121 0l5.646 5.646a.999.999 0 1 1-1.414 1.414l-4.293-4.293v18.586a1 1 0 1 1-2 0V4.414l-4.293 4.293a.999.999 0 0 1-1.414 0ZM24.5 14H22a1 1 0 1 0 0 2h2v13H8V16h2a1 1 0 1 0 0-2H7.5c-.827 0-1.5.673-1.5 1.5v14c0 .827.673 1.5 1.5 1.5h17c.827 0 1.5-.673 1.5-1.5v-14c0-.827-.673-1.5-1.5-1.5Z"
          />
        </svg>
      </span>
      <span class="pf-v6-c-toggle-group__text">Share</span>
    </button>
  </div>
</div>

<br />

<div class="pf-v6-c-toggle-group">
  <div class="pf-v6-c-toggle-group__item">
    <button class="pf-v6-c-toggle-group__button" type="button">
      <span class="pf-v6-c-toggle-group__text">Copy</span>
      <span class="pf-v6-c-toggle-group__icon">
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
            d="M28 7v22.607c0 .768-.622 1.393-1.387 1.393H10a1 1 0 1 1 0-2h16V7a1 1 0 1 1 2 0Zm-6.5 19h-16c-.827 0-1.5-.673-1.5-1.5V8a1.001 1.001 0 0 1 .294-.708l5.998-5.998A1.001 1.001 0 0 1 11 1h10.5c.827 0 1.5.673 1.5 1.5v22c0 .827-.673 1.5-1.5 1.5ZM7.414 7H10V4.414L7.414 7ZM21 3h-9v4.614C12 8.378 11.378 9 10.613 9H6v15h15V3Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <div class="pf-v6-c-toggle-group__item">
    <button class="pf-v6-c-toggle-group__button" type="button">
      <span class="pf-v6-c-toggle-group__text">Undo</span>
      <span class="pf-v6-c-toggle-group__icon">
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
            d="M31 20c0 5.514-4.486 10-10 10H6a1 1 0 1 1 0-2h15c4.411 0 8-3.589 8-8s-3.589-8-8-8H4.414l6.293 6.293a.999.999 0 1 1-1.414 1.414l-7.647-7.646c-.283-.283-.439-.66-.439-1.061s.156-.777.439-1.061l7.646-7.646a.999.999 0 1 1 1.414 1.414L4.413 10h16.586c5.514 0 10 4.486 10 10Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <div class="pf-v6-c-toggle-group__item">
    <button class="pf-v6-c-toggle-group__button pf-m-selected" type="button">
      <span class="pf-v6-c-toggle-group__text">Share</span>
      <span class="pf-v6-c-toggle-group__icon">
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
            d="M9.293 8.707a.999.999 0 0 1 0-1.414l5.646-5.647a1.501 1.501 0 0 1 2.121 0l5.646 5.646a.999.999 0 1 1-1.414 1.414l-4.293-4.293v18.586a1 1 0 1 1-2 0V4.414l-4.293 4.293a.999.999 0 0 1-1.414 0ZM24.5 14H22a1 1 0 1 0 0 2h2v13H8V16h2a1 1 0 1 0 0-2H7.5c-.827 0-1.5.673-1.5 1.5v14c0 .827.673 1.5 1.5 1.5h17c.827 0 1.5-.673 1.5-1.5v-14c0-.827-.673-1.5-1.5-1.5Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

```

### Compact

```html
<div class="pf-v6-c-toggle-group pf-m-compact">
  <div class="pf-v6-c-toggle-group__item">
    <button class="pf-v6-c-toggle-group__button" type="button">
      <span class="pf-v6-c-toggle-group__text">Option 1</span>
    </button>
  </div>
  <div class="pf-v6-c-toggle-group__item">
    <button class="pf-v6-c-toggle-group__button" type="button">
      <span class="pf-v6-c-toggle-group__text">Option 2</span>
    </button>
  </div>
  <div class="pf-v6-c-toggle-group__item">
    <button class="pf-v6-c-toggle-group__button" type="button">
      <span class="pf-v6-c-toggle-group__text">Option 3</span>
    </button>
  </div>
</div>

<br />

<div class="pf-v6-c-toggle-group pf-m-compact">
  <div class="pf-v6-c-toggle-group__item">
    <button class="pf-v6-c-toggle-group__button pf-m-selected" type="button">
      <span class="pf-v6-c-toggle-group__text">Option 1</span>
    </button>
  </div>
  <div class="pf-v6-c-toggle-group__item">
    <button class="pf-v6-c-toggle-group__button pf-m-selected" type="button">
      <span class="pf-v6-c-toggle-group__text">Option 2</span>
    </button>
  </div>
  <div class="pf-v6-c-toggle-group__item">
    <button class="pf-v6-c-toggle-group__button" type="button">
      <span class="pf-v6-c-toggle-group__text">Option 3</span>
    </button>
  </div>
</div>

<br />

<div class="pf-v6-c-toggle-group pf-m-compact">
  <div class="pf-v6-c-toggle-group__item">
    <button class="pf-v6-c-toggle-group__button" type="button">
      <span class="pf-v6-c-toggle-group__text">Option 1</span>
    </button>
  </div>
  <div class="pf-v6-c-toggle-group__item">
    <button class="pf-v6-c-toggle-group__button" type="button">
      <span class="pf-v6-c-toggle-group__text">Option 2</span>
    </button>
  </div>
  <div class="pf-v6-c-toggle-group__item">
    <button class="pf-v6-c-toggle-group__button" type="button" disabled>
      <span class="pf-v6-c-toggle-group__text">Option 3</span>
    </button>
  </div>
</div>

```

### Full width toggle

To make toggle group items fill the available space, use `.pf-m-fill`. In the following example, the toggle group items fill the width of the parent as the window size changes.

```html
<div class="pf-v6-c-toggle-group pf-m-fill">
  <div class="pf-v6-c-toggle-group__item">
    <button class="pf-v6-c-toggle-group__button" type="button">
      <span class="pf-v6-c-toggle-group__text">Option 1</span>
    </button>
  </div>
  <div class="pf-v6-c-toggle-group__item">
    <button class="pf-v6-c-toggle-group__button" type="button">
      <span class="pf-v6-c-toggle-group__text">Option 2</span>
    </button>
  </div>
  <div class="pf-v6-c-toggle-group__item">
    <button class="pf-v6-c-toggle-group__button" type="button">
      <span class="pf-v6-c-toggle-group__text">Option 3</span>
    </button>
  </div>
</div>

<br />

<div class="pf-v6-c-toggle-group pf-m-fill">
  <div class="pf-v6-c-toggle-group__item">
    <button class="pf-v6-c-toggle-group__button pf-m-selected" type="button">
      <span class="pf-v6-c-toggle-group__text">Option 1</span>
    </button>
  </div>
  <div class="pf-v6-c-toggle-group__item">
    <button class="pf-v6-c-toggle-group__button pf-m-selected" type="button">
      <span class="pf-v6-c-toggle-group__text">Option 2</span>
    </button>
  </div>
  <div class="pf-v6-c-toggle-group__item">
    <button class="pf-v6-c-toggle-group__button" type="button">
      <span class="pf-v6-c-toggle-group__text">Option 3</span>
    </button>
  </div>
</div>

<br />

<div class="pf-v6-c-toggle-group pf-m-fill">
  <div class="pf-v6-c-toggle-group__item">
    <button class="pf-v6-c-toggle-group__button" type="button">
      <span class="pf-v6-c-toggle-group__text">Option 1</span>
    </button>
  </div>
  <div class="pf-v6-c-toggle-group__item">
    <button class="pf-v6-c-toggle-group__button" type="button">
      <span class="pf-v6-c-toggle-group__text">Option 2</span>
    </button>
  </div>
  <div class="pf-v6-c-toggle-group__item">
    <button class="pf-v6-c-toggle-group__button" type="button" disabled>
      <span class="pf-v6-c-toggle-group__text">Option 3</span>
    </button>
  </div>
</div>

```

## Documentation

### Accessibility

| Attribute | Applied to | Outcome |
| -- | -- | -- |
| `aria-label="[button label text]"` | `.pf-v6-c-toggle-group__button` | Provides an accessible name for the button when an icon is used instead of text. **Required when icon is used with no supporting text** |
| `disabled` | `.pf-v6-c-toggle-group__button` | When a button element is used, indicates that it is unavailable and removes it from keyboard focus. **Required when button is disabled** |

### Usage

| Class | Applied to | Outcome |
| -- | -- | -- |
| `.pf-v6-c-toggle-group` | `<div>` | Initiates the toggle group. **Required** |
| `.pf-v6-c-toggle-group__button` | `<button>` | Initiates the toggle group button. **Required** |
| `.pf-v6-c-toggle-group__item` | `<div>` | Initiates the toggle group item wrapper. **Required** |
| `.pf-v6-c-toggle-group__text` | `<span>` | Initiates the toggle button text element. |
| `.pf-v6-c-toggle-group__icon` | `<span>` | Initiates the toggle button icon element. |
| `.pf-m-compact` | `.pf-v6-c-toggle-group` | Modifies the toggle group for compact styles. |
| `.pf-m-fill` | `.pf-v6-c-toggle-group` | Modifies the group items to fill the available space. |
| `.pf-m-selected` | `.pf-v6-c-toggle-group__button` | Modifies the toggle button group button for the selected state. |
