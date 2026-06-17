---
id: Button
section: components
cssPrefix: pf-v6-c-button
---import './Button.css'

## Examples

### Variations

```html
<button class="pf-v6-c-button pf-m-primary" type="button">
  <span class="pf-v6-c-button__text">Primary</span>
</button>

<button class="pf-v6-c-button pf-m-secondary" type="button">
  <span class="pf-v6-c-button__text">Secondary</span>
</button>

<button class="pf-v6-c-button pf-m-danger pf-m-secondary" type="button">
  <span class="pf-v6-c-button__text">Secondary danger</span>
</button>

<button class="pf-v6-c-button pf-m-tertiary" type="button">
  <span class="pf-v6-c-button__text">Tertiary</span>
</button>

<button class="pf-v6-c-button pf-m-danger" type="button">
  <span class="pf-v6-c-button__text">Danger</span>
</button>

<button class="pf-v6-c-button pf-m-warning" type="button">
  <span class="pf-v6-c-button__text">Warning</span>
</button>

<br />
<br />

<button class="pf-v6-c-button pf-m-link" type="button">
  <span class="pf-v6-c-button__text">Link</span>
</button>

<button class="pf-v6-c-button pf-m-link pf-m-danger" type="button">
  <span class="pf-v6-c-button__text">Link danger</span>
</button>

<button class="pf-v6-c-button pf-m-inline pf-m-link" type="button">
  <span class="pf-v6-c-button__text">Inline link</span>
</button>

<button class="pf-v6-c-button pf-m-plain" type="button" aria-label="Remove">
  <span class="pf-v6-c-button__icon">
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
        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
      />
    </svg>
  </span>
</button>

<button class="pf-v6-c-button pf-m-plain" type="button" aria-label="Remove">
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Plain with text</span>
</button>

<br />
<br />

<button class="pf-v6-c-button pf-m-control" type="button">
  <span class="pf-v6-c-button__text">Control</span>
</button>

<button
  class="pf-v6-c-button pf-m-control"
  type="button"
  aria-label="Copy input"
>
  <span class="pf-v6-c-button__icon">
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

<br />
<br />

<div>
  <strong>Icon</strong>
</div>
<button class="pf-v6-c-button pf-m-primary" type="button">
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Primary</span>
</button>

<button class="pf-v6-c-button pf-m-secondary" type="button">
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Secondary</span>
</button>

<button class="pf-v6-c-button pf-m-danger pf-m-secondary" type="button">
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Secondary danger</span>
</button>

<button class="pf-v6-c-button pf-m-tertiary" type="button">
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Tertiary</span>
</button>

<button class="pf-v6-c-button pf-m-danger" type="button">
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Danger</span>
</button>

<button class="pf-v6-c-button pf-m-warning" type="button">
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Warning</span>
</button>

<br />
<br />

<button class="pf-v6-c-button pf-m-link" type="button">
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Link</span>
</button>

<button class="pf-v6-c-button pf-m-link pf-m-danger" type="button">
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Link danger</span>
</button>

<button class="pf-v6-c-button pf-m-inline pf-m-link" type="button">
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Inline link</span>
</button>

<button class="pf-v6-c-button pf-m-plain" type="button" aria-label="Remove">
  <span class="pf-v6-c-button__icon">
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
        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
      />
    </svg>
  </span>
</button>

<button class="pf-v6-c-button pf-m-plain" type="button" aria-label="Remove">
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Plain with text</span>
</button>

<br />
<br />

<button class="pf-v6-c-button pf-m-control" type="button">
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Control</span>
</button>

<button
  class="pf-v6-c-button pf-m-control"
  type="button"
  aria-label="Copy input"
>
  <span class="pf-v6-c-button__icon">
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

<br />
<br />

<div>
  <strong>Icon end</strong>
</div>
<button class="pf-v6-c-button pf-m-primary" type="button">
  <span class="pf-v6-c-button__text">Primary</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<button class="pf-v6-c-button pf-m-secondary" type="button">
  <span class="pf-v6-c-button__text">Secondary</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<button class="pf-v6-c-button pf-m-danger pf-m-secondary" type="button">
  <span class="pf-v6-c-button__text">Secondary danger</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<button class="pf-v6-c-button pf-m-tertiary" type="button">
  <span class="pf-v6-c-button__text">Tertiary</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<button class="pf-v6-c-button pf-m-danger" type="button">
  <span class="pf-v6-c-button__text">Danger</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<button class="pf-v6-c-button pf-m-warning" type="button">
  <span class="pf-v6-c-button__text">Warning</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<br />
<br />

<button class="pf-v6-c-button pf-m-link" type="button">
  <span class="pf-v6-c-button__text">Link</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<button class="pf-v6-c-button pf-m-link pf-m-danger" type="button">
  <span class="pf-v6-c-button__text">Link danger</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<button class="pf-v6-c-button pf-m-inline pf-m-link" type="button">
  <span class="pf-v6-c-button__text">Inline link</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<button class="pf-v6-c-button pf-m-plain" type="button" aria-label="Remove">
  <span class="pf-v6-c-button__icon">
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
        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
      />
    </svg>
  </span>
</button>

<button class="pf-v6-c-button pf-m-plain" type="button" aria-label="Remove">
  <span class="pf-v6-c-button__text">Plain with text</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
      />
    </svg>
  </span>
</button>

<br />
<br />

<button class="pf-v6-c-button pf-m-control" type="button">
  <span class="pf-v6-c-button__text">Control</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<button
  class="pf-v6-c-button pf-m-control"
  type="button"
  aria-label="Copy input"
>
  <span class="pf-v6-c-button__icon">
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

```

### Clicked buttons

```html
<button class="pf-v6-c-button pf-m-clicked pf-m-primary" type="button">
  <span class="pf-v6-c-button__text">Primary</span>
</button>

<button class="pf-v6-c-button pf-m-clicked pf-m-secondary" type="button">
  <span class="pf-v6-c-button__text">Secondary</span>
</button>

<button
  class="pf-v6-c-button pf-m-clicked pf-m-danger pf-m-secondary"
  type="button"
>
  <span class="pf-v6-c-button__text">Secondary danger</span>
</button>

<button class="pf-v6-c-button pf-m-clicked pf-m-tertiary" type="button">
  <span class="pf-v6-c-button__text">Tertiary</span>
</button>

<button class="pf-v6-c-button pf-m-clicked pf-m-danger" type="button">
  <span class="pf-v6-c-button__text">Danger</span>
</button>

<button class="pf-v6-c-button pf-m-clicked pf-m-warning" type="button">
  <span class="pf-v6-c-button__text">Warning</span>
</button>

<br />
<br />

<button class="pf-v6-c-button pf-m-clicked pf-m-link" type="button">
  <span class="pf-v6-c-button__text">Link</span>
</button>

<button class="pf-v6-c-button pf-m-clicked pf-m-link pf-m-danger" type="button">
  <span class="pf-v6-c-button__text">Link danger</span>
</button>

<button class="pf-v6-c-button pf-m-clicked pf-m-inline pf-m-link" type="button">
  <span class="pf-v6-c-button__text">Inline link</span>
</button>

<button
  class="pf-v6-c-button pf-m-clicked pf-m-plain"
  type="button"
  aria-label="Remove"
>
  <span class="pf-v6-c-button__icon">
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
        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
      />
    </svg>
  </span>
</button>

<button
  class="pf-v6-c-button pf-m-clicked pf-m-plain"
  type="button"
  aria-label="Remove"
>
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Plain with text</span>
</button>

<br />
<br />

<button class="pf-v6-c-button pf-m-clicked pf-m-control" type="button">
  <span class="pf-v6-c-button__text">Control</span>
</button>

<button
  class="pf-v6-c-button pf-m-clicked pf-m-control"
  type="button"
  aria-label="Copy input"
>
  <span class="pf-v6-c-button__icon">
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

<br />
<br />

<div>
  <strong>Icon</strong>
</div>
<button class="pf-v6-c-button pf-m-clicked pf-m-primary" type="button">
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Primary</span>
</button>

<button class="pf-v6-c-button pf-m-clicked pf-m-secondary" type="button">
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Secondary</span>
</button>

<button
  class="pf-v6-c-button pf-m-clicked pf-m-danger pf-m-secondary"
  type="button"
>
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Secondary danger</span>
</button>

<button class="pf-v6-c-button pf-m-clicked pf-m-tertiary" type="button">
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Tertiary</span>
</button>

<button class="pf-v6-c-button pf-m-clicked pf-m-danger" type="button">
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Danger</span>
</button>

<button class="pf-v6-c-button pf-m-clicked pf-m-warning" type="button">
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Warning</span>
</button>

<br />
<br />

<button class="pf-v6-c-button pf-m-clicked pf-m-link" type="button">
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Link</span>
</button>

<button class="pf-v6-c-button pf-m-clicked pf-m-link pf-m-danger" type="button">
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Link danger</span>
</button>

<button class="pf-v6-c-button pf-m-clicked pf-m-inline pf-m-link" type="button">
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Inline link</span>
</button>

<button
  class="pf-v6-c-button pf-m-clicked pf-m-plain"
  type="button"
  aria-label="Remove"
>
  <span class="pf-v6-c-button__icon">
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
        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
      />
    </svg>
  </span>
</button>

<button
  class="pf-v6-c-button pf-m-clicked pf-m-plain"
  type="button"
  aria-label="Remove"
>
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Plain with text</span>
</button>

<br />
<br />

<button class="pf-v6-c-button pf-m-clicked pf-m-control" type="button">
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Control</span>
</button>

<button
  class="pf-v6-c-button pf-m-clicked pf-m-control"
  type="button"
  aria-label="Copy input"
>
  <span class="pf-v6-c-button__icon">
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

<br />
<br />

<div>
  <strong>Icon end</strong>
</div>
<button class="pf-v6-c-button pf-m-clicked pf-m-primary" type="button">
  <span class="pf-v6-c-button__text">Primary</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<button class="pf-v6-c-button pf-m-clicked pf-m-secondary" type="button">
  <span class="pf-v6-c-button__text">Secondary</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<button
  class="pf-v6-c-button pf-m-clicked pf-m-danger pf-m-secondary"
  type="button"
>
  <span class="pf-v6-c-button__text">Secondary danger</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<button class="pf-v6-c-button pf-m-clicked pf-m-tertiary" type="button">
  <span class="pf-v6-c-button__text">Tertiary</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<button class="pf-v6-c-button pf-m-clicked pf-m-danger" type="button">
  <span class="pf-v6-c-button__text">Danger</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<button class="pf-v6-c-button pf-m-clicked pf-m-warning" type="button">
  <span class="pf-v6-c-button__text">Warning</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<br />
<br />

<button class="pf-v6-c-button pf-m-clicked pf-m-link" type="button">
  <span class="pf-v6-c-button__text">Link</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<button class="pf-v6-c-button pf-m-clicked pf-m-link pf-m-danger" type="button">
  <span class="pf-v6-c-button__text">Link danger</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<button class="pf-v6-c-button pf-m-clicked pf-m-inline pf-m-link" type="button">
  <span class="pf-v6-c-button__text">Inline link</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<button
  class="pf-v6-c-button pf-m-clicked pf-m-plain"
  type="button"
  aria-label="Remove"
>
  <span class="pf-v6-c-button__icon">
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
        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
      />
    </svg>
  </span>
</button>

<button
  class="pf-v6-c-button pf-m-clicked pf-m-plain"
  type="button"
  aria-label="Remove"
>
  <span class="pf-v6-c-button__text">Plain with text</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
      />
    </svg>
  </span>
</button>

<br />
<br />

<button class="pf-v6-c-button pf-m-clicked pf-m-control" type="button">
  <span class="pf-v6-c-button__text">Control</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<button
  class="pf-v6-c-button pf-m-clicked pf-m-control"
  type="button"
  aria-label="Copy input"
>
  <span class="pf-v6-c-button__icon">
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

```

### Small buttons

```html
<button class="pf-v6-c-button pf-m-small pf-m-primary" type="button">
  <span class="pf-v6-c-button__text">Primary</span>
</button>

<button class="pf-v6-c-button pf-m-small pf-m-secondary" type="button">
  <span class="pf-v6-c-button__text">Secondary</span>
</button>

<button
  class="pf-v6-c-button pf-m-small pf-m-danger pf-m-secondary"
  type="button"
>
  <span class="pf-v6-c-button__text">Secondary danger</span>
</button>

<button class="pf-v6-c-button pf-m-small pf-m-tertiary" type="button">
  <span class="pf-v6-c-button__text">Tertiary</span>
</button>

<button class="pf-v6-c-button pf-m-small pf-m-danger" type="button">
  <span class="pf-v6-c-button__text">Danger</span>
</button>

<button class="pf-v6-c-button pf-m-small pf-m-warning" type="button">
  <span class="pf-v6-c-button__text">Warning</span>
</button>

<br />
<br />

<button class="pf-v6-c-button pf-m-small pf-m-link" type="button">
  <span class="pf-v6-c-button__text">Link</span>
</button>

<button class="pf-v6-c-button pf-m-small pf-m-link pf-m-danger" type="button">
  <span class="pf-v6-c-button__text">Link danger</span>
</button>

<button class="pf-v6-c-button pf-m-small pf-m-inline pf-m-link" type="button">
  <span class="pf-v6-c-button__text">Inline link</span>
</button>

<button
  class="pf-v6-c-button pf-m-small pf-m-plain"
  type="button"
  aria-label="Remove"
>
  <span class="pf-v6-c-button__icon">
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
        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
      />
    </svg>
  </span>
</button>

<button
  class="pf-v6-c-button pf-m-small pf-m-plain"
  type="button"
  aria-label="Remove"
>
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Plain with text</span>
</button>

<br />
<br />

<button class="pf-v6-c-button pf-m-small pf-m-control" type="button">
  <span class="pf-v6-c-button__text">Control</span>
</button>

<button
  class="pf-v6-c-button pf-m-small pf-m-control"
  type="button"
  aria-label="Copy input"
>
  <span class="pf-v6-c-button__icon">
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

<br />
<br />

<div>
  <strong>Icon</strong>
</div>
<button class="pf-v6-c-button pf-m-small pf-m-primary" type="button">
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Primary</span>
</button>

<button class="pf-v6-c-button pf-m-small pf-m-secondary" type="button">
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Secondary</span>
</button>

<button
  class="pf-v6-c-button pf-m-small pf-m-danger pf-m-secondary"
  type="button"
>
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Secondary danger</span>
</button>

<button class="pf-v6-c-button pf-m-small pf-m-tertiary" type="button">
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Tertiary</span>
</button>

<button class="pf-v6-c-button pf-m-small pf-m-danger" type="button">
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Danger</span>
</button>

<button class="pf-v6-c-button pf-m-small pf-m-warning" type="button">
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Warning</span>
</button>

<br />
<br />

<button class="pf-v6-c-button pf-m-small pf-m-link" type="button">
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Link</span>
</button>

<button class="pf-v6-c-button pf-m-small pf-m-link pf-m-danger" type="button">
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Link danger</span>
</button>

<button class="pf-v6-c-button pf-m-small pf-m-inline pf-m-link" type="button">
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Inline link</span>
</button>

<button
  class="pf-v6-c-button pf-m-small pf-m-plain"
  type="button"
  aria-label="Remove"
>
  <span class="pf-v6-c-button__icon">
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
        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
      />
    </svg>
  </span>
</button>

<button
  class="pf-v6-c-button pf-m-small pf-m-plain"
  type="button"
  aria-label="Remove"
>
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Plain with text</span>
</button>

<br />
<br />

<button class="pf-v6-c-button pf-m-small pf-m-control" type="button">
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Control</span>
</button>

<button
  class="pf-v6-c-button pf-m-small pf-m-control"
  type="button"
  aria-label="Copy input"
>
  <span class="pf-v6-c-button__icon">
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

<br />
<br />

<div>
  <strong>Icon end</strong>
</div>
<button class="pf-v6-c-button pf-m-small pf-m-primary" type="button">
  <span class="pf-v6-c-button__text">Primary</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<button class="pf-v6-c-button pf-m-small pf-m-secondary" type="button">
  <span class="pf-v6-c-button__text">Secondary</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<button
  class="pf-v6-c-button pf-m-small pf-m-danger pf-m-secondary"
  type="button"
>
  <span class="pf-v6-c-button__text">Secondary danger</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<button class="pf-v6-c-button pf-m-small pf-m-tertiary" type="button">
  <span class="pf-v6-c-button__text">Tertiary</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<button class="pf-v6-c-button pf-m-small pf-m-danger" type="button">
  <span class="pf-v6-c-button__text">Danger</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<button class="pf-v6-c-button pf-m-small pf-m-warning" type="button">
  <span class="pf-v6-c-button__text">Warning</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<br />
<br />

<button class="pf-v6-c-button pf-m-small pf-m-link" type="button">
  <span class="pf-v6-c-button__text">Link</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<button class="pf-v6-c-button pf-m-small pf-m-link pf-m-danger" type="button">
  <span class="pf-v6-c-button__text">Link danger</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<button class="pf-v6-c-button pf-m-small pf-m-inline pf-m-link" type="button">
  <span class="pf-v6-c-button__text">Inline link</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<button
  class="pf-v6-c-button pf-m-small pf-m-plain"
  type="button"
  aria-label="Remove"
>
  <span class="pf-v6-c-button__icon">
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
        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
      />
    </svg>
  </span>
</button>

<button
  class="pf-v6-c-button pf-m-small pf-m-plain"
  type="button"
  aria-label="Remove"
>
  <span class="pf-v6-c-button__text">Plain with text</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
      />
    </svg>
  </span>
</button>

<br />
<br />

<button class="pf-v6-c-button pf-m-small pf-m-control" type="button">
  <span class="pf-v6-c-button__text">Control</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<button
  class="pf-v6-c-button pf-m-small pf-m-control"
  type="button"
  aria-label="Copy input"
>
  <span class="pf-v6-c-button__icon">
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

```

### Disabled

```html
<button class="pf-v6-c-button pf-m-primary" type="button" disabled>
  <span class="pf-v6-c-button__text">Primary</span>
</button>

<button class="pf-v6-c-button pf-m-secondary" type="button" disabled>
  <span class="pf-v6-c-button__text">Secondary</span>
</button>

<button
  class="pf-v6-c-button pf-m-danger pf-m-secondary"
  type="button"
  disabled
>
  <span class="pf-v6-c-button__text">Secondary danger</span>
</button>

<button class="pf-v6-c-button pf-m-tertiary" type="button" disabled>
  <span class="pf-v6-c-button__text">Tertiary</span>
</button>

<button class="pf-v6-c-button pf-m-danger" type="button" disabled>
  <span class="pf-v6-c-button__text">Danger</span>
</button>

<button class="pf-v6-c-button pf-m-warning" type="button" disabled>
  <span class="pf-v6-c-button__text">Warning</span>
</button>

<br />
<br />

<button class="pf-v6-c-button pf-m-link" type="button" disabled>
  <span class="pf-v6-c-button__text">Link</span>
</button>

<button class="pf-v6-c-button pf-m-link pf-m-danger" type="button" disabled>
  <span class="pf-v6-c-button__text">Link danger</span>
</button>

<button class="pf-v6-c-button pf-m-inline pf-m-link" type="button" disabled>
  <span class="pf-v6-c-button__text">Inline link</span>
</button>

<button
  class="pf-v6-c-button pf-m-plain"
  type="button"
  aria-label="Remove"
  disabled
>
  <span class="pf-v6-c-button__icon">
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
        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
      />
    </svg>
  </span>
</button>

<button
  class="pf-v6-c-button pf-m-plain"
  type="button"
  aria-label="Remove"
  disabled
>
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Plain with text</span>
</button>

<br />
<br />

<button class="pf-v6-c-button pf-m-control" type="button" disabled>
  <span class="pf-v6-c-button__text">Control</span>
</button>

<button
  class="pf-v6-c-button pf-m-control"
  type="button"
  aria-label="Copy input"
  disabled
>
  <span class="pf-v6-c-button__icon">
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

<br />
<br />

<div>
  <strong>Icon</strong>
</div>
<button class="pf-v6-c-button pf-m-primary" type="button" disabled>
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Primary</span>
</button>

<button class="pf-v6-c-button pf-m-secondary" type="button" disabled>
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Secondary</span>
</button>

<button
  class="pf-v6-c-button pf-m-danger pf-m-secondary"
  type="button"
  disabled
>
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Secondary danger</span>
</button>

<button class="pf-v6-c-button pf-m-tertiary" type="button" disabled>
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Tertiary</span>
</button>

<button class="pf-v6-c-button pf-m-danger" type="button" disabled>
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Danger</span>
</button>

<button class="pf-v6-c-button pf-m-warning" type="button" disabled>
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Warning</span>
</button>

<br />
<br />

<button class="pf-v6-c-button pf-m-link" type="button" disabled>
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Link</span>
</button>

<button class="pf-v6-c-button pf-m-link pf-m-danger" type="button" disabled>
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Link danger</span>
</button>

<button class="pf-v6-c-button pf-m-inline pf-m-link" type="button" disabled>
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Inline link</span>
</button>

<button
  class="pf-v6-c-button pf-m-plain"
  type="button"
  aria-label="Remove"
  disabled
>
  <span class="pf-v6-c-button__icon">
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
        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
      />
    </svg>
  </span>
</button>

<button
  class="pf-v6-c-button pf-m-plain"
  type="button"
  aria-label="Remove"
  disabled
>
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Plain with text</span>
</button>

<br />
<br />

<button class="pf-v6-c-button pf-m-control" type="button" disabled>
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Control</span>
</button>

<button
  class="pf-v6-c-button pf-m-control"
  type="button"
  aria-label="Copy input"
  disabled
>
  <span class="pf-v6-c-button__icon">
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

<br />
<br />

<div>
  <strong>Icon end</strong>
</div>
<button class="pf-v6-c-button pf-m-primary" type="button" disabled>
  <span class="pf-v6-c-button__text">Primary</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<button class="pf-v6-c-button pf-m-secondary" type="button" disabled>
  <span class="pf-v6-c-button__text">Secondary</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<button
  class="pf-v6-c-button pf-m-danger pf-m-secondary"
  type="button"
  disabled
>
  <span class="pf-v6-c-button__text">Secondary danger</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<button class="pf-v6-c-button pf-m-tertiary" type="button" disabled>
  <span class="pf-v6-c-button__text">Tertiary</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<button class="pf-v6-c-button pf-m-danger" type="button" disabled>
  <span class="pf-v6-c-button__text">Danger</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<button class="pf-v6-c-button pf-m-warning" type="button" disabled>
  <span class="pf-v6-c-button__text">Warning</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<br />
<br />

<button class="pf-v6-c-button pf-m-link" type="button" disabled>
  <span class="pf-v6-c-button__text">Link</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<button class="pf-v6-c-button pf-m-link pf-m-danger" type="button" disabled>
  <span class="pf-v6-c-button__text">Link danger</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<button class="pf-v6-c-button pf-m-inline pf-m-link" type="button" disabled>
  <span class="pf-v6-c-button__text">Inline link</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<button
  class="pf-v6-c-button pf-m-plain"
  type="button"
  aria-label="Remove"
  disabled
>
  <span class="pf-v6-c-button__icon">
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
        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
      />
    </svg>
  </span>
</button>

<button
  class="pf-v6-c-button pf-m-plain"
  type="button"
  aria-label="Remove"
  disabled
>
  <span class="pf-v6-c-button__text">Plain with text</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
      />
    </svg>
  </span>
</button>

<br />
<br />

<button class="pf-v6-c-button pf-m-control" type="button" disabled>
  <span class="pf-v6-c-button__text">Control</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<button
  class="pf-v6-c-button pf-m-control"
  type="button"
  aria-label="Copy input"
  disabled
>
  <span class="pf-v6-c-button__icon">
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

```

### Aria-disabled

```html
<button
  class="pf-v6-c-button pf-m-aria-disabled pf-m-primary"
  type="button"
  aria-disabled="true"
>
  <span class="pf-v6-c-button__text">Primary</span>
</button>

<button
  class="pf-v6-c-button pf-m-aria-disabled pf-m-secondary"
  type="button"
  aria-disabled="true"
>
  <span class="pf-v6-c-button__text">Secondary</span>
</button>

<button
  class="pf-v6-c-button pf-m-aria-disabled pf-m-danger pf-m-secondary"
  type="button"
  aria-disabled="true"
>
  <span class="pf-v6-c-button__text">Secondary danger</span>
</button>

<button
  class="pf-v6-c-button pf-m-aria-disabled pf-m-tertiary"
  type="button"
  aria-disabled="true"
>
  <span class="pf-v6-c-button__text">Tertiary</span>
</button>

<button
  class="pf-v6-c-button pf-m-aria-disabled pf-m-danger"
  type="button"
  aria-disabled="true"
>
  <span class="pf-v6-c-button__text">Danger</span>
</button>

<button
  class="pf-v6-c-button pf-m-aria-disabled pf-m-warning"
  type="button"
  aria-disabled="true"
>
  <span class="pf-v6-c-button__text">Warning</span>
</button>

<br />
<br />

<button
  class="pf-v6-c-button pf-m-aria-disabled pf-m-link"
  type="button"
  aria-disabled="true"
>
  <span class="pf-v6-c-button__text">Link</span>
</button>

<button
  class="pf-v6-c-button pf-m-aria-disabled pf-m-link pf-m-danger"
  type="button"
  aria-disabled="true"
>
  <span class="pf-v6-c-button__text">Link danger</span>
</button>

<button
  class="pf-v6-c-button pf-m-aria-disabled pf-m-inline pf-m-link"
  type="button"
  aria-disabled="true"
>
  <span class="pf-v6-c-button__text">Inline link</span>
</button>

<button
  class="pf-v6-c-button pf-m-aria-disabled pf-m-plain"
  type="button"
  aria-label="Remove"
  aria-disabled="true"
>
  <span class="pf-v6-c-button__icon">
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
        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
      />
    </svg>
  </span>
</button>

<button
  class="pf-v6-c-button pf-m-aria-disabled pf-m-plain"
  type="button"
  aria-label="Remove"
  aria-disabled="true"
>
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Plain with text</span>
</button>

<br />
<br />

<button
  class="pf-v6-c-button pf-m-aria-disabled pf-m-control"
  type="button"
  aria-disabled="true"
>
  <span class="pf-v6-c-button__text">Control</span>
</button>

<button
  class="pf-v6-c-button pf-m-aria-disabled pf-m-control"
  type="button"
  aria-label="Copy input"
  aria-disabled="true"
>
  <span class="pf-v6-c-button__icon">
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

<br />
<br />

<div>
  <strong>Icon</strong>
</div>
<button
  class="pf-v6-c-button pf-m-aria-disabled pf-m-primary"
  type="button"
  aria-disabled="true"
>
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Primary</span>
</button>

<button
  class="pf-v6-c-button pf-m-aria-disabled pf-m-secondary"
  type="button"
  aria-disabled="true"
>
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Secondary</span>
</button>

<button
  class="pf-v6-c-button pf-m-aria-disabled pf-m-danger pf-m-secondary"
  type="button"
  aria-disabled="true"
>
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Secondary danger</span>
</button>

<button
  class="pf-v6-c-button pf-m-aria-disabled pf-m-tertiary"
  type="button"
  aria-disabled="true"
>
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Tertiary</span>
</button>

<button
  class="pf-v6-c-button pf-m-aria-disabled pf-m-danger"
  type="button"
  aria-disabled="true"
>
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Danger</span>
</button>

<button
  class="pf-v6-c-button pf-m-aria-disabled pf-m-warning"
  type="button"
  aria-disabled="true"
>
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Warning</span>
</button>

<br />
<br />

<button
  class="pf-v6-c-button pf-m-aria-disabled pf-m-link"
  type="button"
  aria-disabled="true"
>
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Link</span>
</button>

<button
  class="pf-v6-c-button pf-m-aria-disabled pf-m-link pf-m-danger"
  type="button"
  aria-disabled="true"
>
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Link danger</span>
</button>

<button
  class="pf-v6-c-button pf-m-aria-disabled pf-m-inline pf-m-link"
  type="button"
  aria-disabled="true"
>
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Inline link</span>
</button>

<button
  class="pf-v6-c-button pf-m-aria-disabled pf-m-plain"
  type="button"
  aria-label="Remove"
  aria-disabled="true"
>
  <span class="pf-v6-c-button__icon">
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
        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
      />
    </svg>
  </span>
</button>

<button
  class="pf-v6-c-button pf-m-aria-disabled pf-m-plain"
  type="button"
  aria-label="Remove"
  aria-disabled="true"
>
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Plain with text</span>
</button>

<br />
<br />

<button
  class="pf-v6-c-button pf-m-aria-disabled pf-m-control"
  type="button"
  aria-disabled="true"
>
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">Control</span>
</button>

<button
  class="pf-v6-c-button pf-m-aria-disabled pf-m-control"
  type="button"
  aria-label="Copy input"
  aria-disabled="true"
>
  <span class="pf-v6-c-button__icon">
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

<br />
<br />

<div>
  <strong>Icon end</strong>
</div>
<button
  class="pf-v6-c-button pf-m-aria-disabled pf-m-primary"
  type="button"
  aria-disabled="true"
>
  <span class="pf-v6-c-button__text">Primary</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<button
  class="pf-v6-c-button pf-m-aria-disabled pf-m-secondary"
  type="button"
  aria-disabled="true"
>
  <span class="pf-v6-c-button__text">Secondary</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<button
  class="pf-v6-c-button pf-m-aria-disabled pf-m-danger pf-m-secondary"
  type="button"
  aria-disabled="true"
>
  <span class="pf-v6-c-button__text">Secondary danger</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<button
  class="pf-v6-c-button pf-m-aria-disabled pf-m-tertiary"
  type="button"
  aria-disabled="true"
>
  <span class="pf-v6-c-button__text">Tertiary</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<button
  class="pf-v6-c-button pf-m-aria-disabled pf-m-danger"
  type="button"
  aria-disabled="true"
>
  <span class="pf-v6-c-button__text">Danger</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<button
  class="pf-v6-c-button pf-m-aria-disabled pf-m-warning"
  type="button"
  aria-disabled="true"
>
  <span class="pf-v6-c-button__text">Warning</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<br />
<br />

<button
  class="pf-v6-c-button pf-m-aria-disabled pf-m-link"
  type="button"
  aria-disabled="true"
>
  <span class="pf-v6-c-button__text">Link</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<button
  class="pf-v6-c-button pf-m-aria-disabled pf-m-link pf-m-danger"
  type="button"
  aria-disabled="true"
>
  <span class="pf-v6-c-button__text">Link danger</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<button
  class="pf-v6-c-button pf-m-aria-disabled pf-m-inline pf-m-link"
  type="button"
  aria-disabled="true"
>
  <span class="pf-v6-c-button__text">Inline link</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<button
  class="pf-v6-c-button pf-m-aria-disabled pf-m-plain"
  type="button"
  aria-label="Remove"
  aria-disabled="true"
>
  <span class="pf-v6-c-button__icon">
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
        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
      />
    </svg>
  </span>
</button>

<button
  class="pf-v6-c-button pf-m-aria-disabled pf-m-plain"
  type="button"
  aria-label="Remove"
  aria-disabled="true"
>
  <span class="pf-v6-c-button__text">Plain with text</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
      />
    </svg>
  </span>
</button>

<br />
<br />

<button
  class="pf-v6-c-button pf-m-aria-disabled pf-m-control"
  type="button"
  aria-disabled="true"
>
  <span class="pf-v6-c-button__text">Control</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<button
  class="pf-v6-c-button pf-m-aria-disabled pf-m-control"
  type="button"
  aria-label="Copy input"
  aria-disabled="true"
>
  <span class="pf-v6-c-button__icon">
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

```

### Links as buttons

```html
<a
  class="pf-v6-c-button pf-m-primary"
  href="https://www.w3.org/TR/WCAG20-TECHS/ARIA8.html#ARIA8-examples"
>
  <span class="pf-v6-c-button__text">Primary link to W3.org</span>
</a>

<a
  class="pf-v6-c-button pf-m-secondary"
  aria-label="Read more about button documentation"
  href="#overview"
>
  <span class="pf-v6-c-button__text">Secondary link to anchor</span>
</a>

<a
  class="pf-v6-c-button pf-m-danger pf-m-secondary"
  aria-label="Read more about button documentation"
  href="#overview"
>
  <span class="pf-v6-c-button__text">Secondary danger link to anchor</span>
</a>

<a
  class="pf-v6-c-button pf-m-tertiary pf-m-disabled"
  href="https://www.w3.org/TR/WCAG20-TECHS/ARIA8.html#ARIA8-examples"
  aria-disabled="true"
  tabindex="-1"
>
  <span class="pf-v6-c-button__text">Tertiary link to W3.org</span>
</a>

<a
  class="pf-v6-c-button pf-m-link"
  href="https://www.w3.org/TR/WCAG20-TECHS/ARIA8.html#ARIA8-examples"
>
  <span class="pf-v6-c-button__text">Link to W3.org</span>
</a>

<a
  class="pf-v6-c-button pf-m-link pf-m-danger"
  href="https://www.w3.org/TR/WCAG20-TECHS/ARIA8.html#ARIA8-examples"
>
  <span class="pf-v6-c-button__text">Link danger to W3.org</span>
</a>

```

### Inline link as span

```html
<strong>Plain</strong>
<br />
<span
  class="pf-v6-c-button pf-m-plain"
  type="button"
  role="button"
  tabindex="0"
  aria-label="Remove"
>
  <span class="pf-v6-c-button__icon">
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
        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
      />
    </svg>
  </span>
</span>
<br />
<br />
<strong>Plain no padding</strong>
<br />
<span
  class="pf-v6-c-button pf-m-no-padding pf-m-plain"
  type="button"
  role="button"
  tabindex="0"
  aria-label="Remove"
>
  <span class="pf-v6-c-button__icon">
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
        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
      />
    </svg>
  </span>
</span>
<br />
<br />
<strong>Inline link</strong>
<br />Lorem ipsum dolor sit amet, consectetur adipiscing elit.
<span
  class="pf-v6-c-button pf-m-inline pf-m-link"
  type="button"
  role="button"
  tabindex="0"
>
  <span
    class="pf-v6-c-button__text"
  >This is long button text that needs to be a span so that it will wrap inline with the text around it.</span>
</span>
Sed hendrerit nisi in cursus maximus. Ut malesuada nisi turpis, in condimentum velit elementum non.

```

### Block level

```html
<button class="pf-v6-c-button pf-m-block pf-m-primary" type="button">
  <span class="pf-v6-c-button__text">Block level button</span>
</button>

```

### Types

```html
<button class="pf-v6-c-button pf-m-primary" type="submit">
  <span class="pf-v6-c-button__text">Submit</span>
</button>

<button class="pf-v6-c-button pf-m-primary" type="reset">
  <span class="pf-v6-c-button__text">Reset</span>
</button>

<button class="pf-v6-c-button pf-m-primary" type="button">
  <span class="pf-v6-c-button__text">Default</span>
</button>

```

### Call to action

```html
<button class="pf-v6-c-button pf-m-display-lg pf-m-primary" type="button">
  <span class="pf-v6-c-button__text">Call to action</span>
</button>

<button class="pf-v6-c-button pf-m-display-lg pf-m-secondary" type="button">
  <span class="pf-v6-c-button__text">Call to action</span>
</button>

<button class="pf-v6-c-button pf-m-display-lg pf-m-tertiary" type="button">
  <span class="pf-v6-c-button__text">Call to action</span>
</button>

<button class="pf-v6-c-button pf-m-display-lg pf-m-link" type="button">
  <span class="pf-v6-c-button__text">Call to action</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M30.354 14.939 19.708 4.293a.999.999 0 1 0-1.414 1.414L27.587 15H2a1 1 0 0 0 0 2h25.586l-9.293 9.293a.999.999 0 1 0 1.414 1.414l10.646-10.646c.283-.283.439-.66.439-1.061s-.156-.777-.439-1.061Z"
      />
    </svg>
  </span>
</button>

<button
  class="pf-v6-c-button pf-m-display-lg pf-m-inline pf-m-link"
  type="button"
>
  <span class="pf-v6-c-button__text">Call to action</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M30.354 14.939 19.708 4.293a.999.999 0 1 0-1.414 1.414L27.587 15H2a1 1 0 0 0 0 2h25.586l-9.293 9.293a.999.999 0 1 0 1.414 1.414l10.646-10.646c.283-.283.439-.66.439-1.061s-.156-.777-.439-1.061Z"
      />
    </svg>
  </span>
</button>
<br />
<br />
<strong>disabled</strong>
<br />
<button
  class="pf-v6-c-button pf-m-display-lg pf-m-primary"
  type="button"
  disabled
>
  <span class="pf-v6-c-button__text">Call to action</span>
</button>

<button
  class="pf-v6-c-button pf-m-display-lg pf-m-secondary"
  type="button"
  disabled
>
  <span class="pf-v6-c-button__text">Call to action</span>
</button>

<button
  class="pf-v6-c-button pf-m-display-lg pf-m-tertiary"
  type="button"
  disabled
>
  <span class="pf-v6-c-button__text">Call to action</span>
</button>

<button class="pf-v6-c-button pf-m-display-lg pf-m-link" type="button" disabled>
  <span class="pf-v6-c-button__text">Call to action</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M30.354 14.939 19.708 4.293a.999.999 0 1 0-1.414 1.414L27.587 15H2a1 1 0 0 0 0 2h25.586l-9.293 9.293a.999.999 0 1 0 1.414 1.414l10.646-10.646c.283-.283.439-.66.439-1.061s-.156-.777-.439-1.061Z"
      />
    </svg>
  </span>
</button>

<button
  class="pf-v6-c-button pf-m-display-lg pf-m-inline pf-m-link"
  type="button"
  disabled
>
  <span class="pf-v6-c-button__text">Call to action</span>
  <span class="pf-v6-c-button__icon pf-m-end">
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
        d="M30.354 14.939 19.708 4.293a.999.999 0 1 0-1.414 1.414L27.587 15H2a1 1 0 0 0 0 2h25.586l-9.293 9.293a.999.999 0 1 0 1.414 1.414l10.646-10.646c.283-.283.439-.66.439-1.061s-.156-.777-.439-1.061Z"
      />
    </svg>
  </span>
</button>

```

### Progress

```html
<button class="pf-v6-c-button pf-m-progress pf-m-primary" type="button">
  <span class="pf-v6-c-button__text">Primary loader</span>
</button>

<button
  class="pf-v6-c-button pf-m-in-progress pf-m-progress pf-m-primary"
  type="button"
>
  <span class="pf-v6-c-button__progress">
    <svg
      class="pf-v6-c-spinner pf-m-md"
      role="progressbar"
      viewBox="0 0 100 100"
      aria-label="Loading..."
    >
      <circle class="pf-v6-c-spinner__path" cx="50" cy="50" r="45" fill="none" />
    </svg>
  </span>

  <span class="pf-v6-c-button__text">Primary loading</span>
</button>
<br />
<button class="pf-v6-c-button pf-m-progress pf-m-secondary" type="button">
  <span class="pf-v6-c-button__text">Secondary loader</span>
</button>

<button
  class="pf-v6-c-button pf-m-in-progress pf-m-progress pf-m-secondary"
  type="button"
>
  <span class="pf-v6-c-button__progress">
    <svg
      class="pf-v6-c-spinner pf-m-md"
      role="progressbar"
      viewBox="0 0 100 100"
      aria-label="Loading..."
    >
      <circle class="pf-v6-c-spinner__path" cx="50" cy="50" r="45" fill="none" />
    </svg>
  </span>

  <span class="pf-v6-c-button__text">Secondary loading</span>
</button>
<br />
<button class="pf-v6-c-button pf-m-plain" type="button" aria-label="Upload">
  <span class="pf-v6-c-button__icon">
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
        d="M30 29a1 1 0 0 1-1 1H3a1 1 0 1 1 0-2h26a1 1 0 0 1 1 1ZM7.707 12.707 15 5.414V24a1 1 0 1 0 2 0V5.414l7.293 7.293a.997.997 0 0 0 1.414 0 .999.999 0 0 0 0-1.414l-8.646-8.647a1.5 1.5 0 0 0-2.121 0l-8.647 8.647a.999.999 0 1 0 1.414 1.414Z"
      />
    </svg>
  </span>
</button>

<button class="pf-v6-c-button pf-m-in-progress pf-m-plain" type="button">
  <span class="pf-v6-c-button__progress">
    <svg
      class="pf-v6-c-spinner pf-m-md"
      role="progressbar"
      viewBox="0 0 100 100"
      aria-label="Uploading..."
    >
      <circle class="pf-v6-c-spinner__path" cx="50" cy="50" r="45" fill="none" />
    </svg>
  </span>

  <span class="pf-v6-c-button__icon">
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
        d="M30 29a1 1 0 0 1-1 1H3a1 1 0 1 1 0-2h26a1 1 0 0 1 1 1ZM7.707 12.707 15 5.414V24a1 1 0 1 0 2 0V5.414l7.293 7.293a.997.997 0 0 0 1.414 0 .999.999 0 0 0 0-1.414l-8.646-8.647a1.5 1.5 0 0 0-2.121 0l-8.647 8.647a.999.999 0 1 0 1.414 1.414Z"
      />
    </svg>
  </span>
</button>
<br />
<button
  class="pf-v6-c-button pf-m-progress pf-m-inline pf-m-link"
  type="button"
>
  <span class="pf-v6-c-button__text">Inline loader</span>
</button>

<button
  class="pf-v6-c-button pf-m-in-progress pf-m-progress pf-m-inline pf-m-link"
  type="button"
>
  <span class="pf-v6-c-button__progress">
    <svg
      class="pf-v6-c-spinner pf-m-inline"
      role="progressbar"
      viewBox="0 0 100 100"
      aria-label="Loading..."
    >
      <circle class="pf-v6-c-spinner__path" cx="50" cy="50" r="45" fill="none" />
    </svg>
  </span>

  <span class="pf-v6-c-button__text">Inline loading</span>
</button>

```

### Circle buttons

```html isBeta
<button
  class="pf-v6-c-button pf-m-circle pf-m-primary"
  type="button"
  aria-label="Add primary circle variant"
>
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<button
  class="pf-v6-c-button pf-m-circle pf-m-secondary"
  type="button"
  aria-label="Add secondary circle variant"
>
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<button
  class="pf-v6-c-button pf-m-circle pf-m-tertiary"
  type="button"
  aria-label="Add tertiary circle variant"
>
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<button
  class="pf-v6-c-button pf-m-circle pf-m-danger"
  type="button"
  aria-label="Add danger circle variant"
>
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<button
  class="pf-v6-c-button pf-m-circle pf-m-warning"
  type="button"
  aria-label="Add warning circle variant"
>
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<button
  class="pf-v6-c-button pf-m-circle pf-m-link"
  type="button"
  aria-label="Add link circle variant"
>
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm8-13a1 1 0 0 1-1 1h-6v6a1 1 0 0 1-2 0v-6H9a1 1 0 0 1 0-2h6V9a1 1 0 0 1 2 0v6h6a1 1 0 0 1 1 1Z"
      />
    </svg>
  </span>
</button>

<button
  class="pf-v6-c-button pf-m-circle pf-m-plain"
  type="button"
  aria-label="Remove plain circle variant"
>
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
      />
    </svg>
  </span>
</button>

<button
  class="pf-v6-c-button pf-m-circle pf-m-control"
  type="button"
  aria-label="Copy control circle variant"
>
  <span class="pf-v6-c-button__icon pf-m-start">
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

<button
  class="pf-v6-c-button pf-m-circle pf-m-plain"
  type="button"
  aria-label="Upload circle variant"
>
  <span class="pf-v6-c-button__icon">
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
        d="M30 29a1 1 0 0 1-1 1H3a1 1 0 1 1 0-2h26a1 1 0 0 1 1 1ZM7.707 12.707 15 5.414V24a1 1 0 1 0 2 0V5.414l7.293 7.293a.997.997 0 0 0 1.414 0 .999.999 0 0 0 0-1.414l-8.646-8.647a1.5 1.5 0 0 0-2.121 0l-8.647 8.647a.999.999 0 1 0 1.414 1.414Z"
      />
    </svg>
  </span>
</button>

<button
  class="pf-v6-c-button pf-m-circle pf-m-in-progress pf-m-plain"
  type="button"
>
  <span class="pf-v6-c-button__progress">
    <svg
      class="pf-v6-c-spinner pf-m-md"
      role="progressbar"
      viewBox="0 0 100 100"
      aria-label="Uploading circle variant..."
    >
      <circle class="pf-v6-c-spinner__path" cx="50" cy="50" r="45" fill="none" />
    </svg>
  </span>

  <span class="pf-v6-c-button__icon">
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
        d="M30 29a1 1 0 0 1-1 1H3a1 1 0 1 1 0-2h26a1 1 0 0 1 1 1ZM7.707 12.707 15 5.414V24a1 1 0 1 0 2 0V5.414l7.293 7.293a.997.997 0 0 0 1.414 0 .999.999 0 0 0 0-1.414l-8.646-8.647a1.5 1.5 0 0 0-2.121 0l-8.647 8.647a.999.999 0 1 0 1.414 1.414Z"
      />
    </svg>
  </span>
</button>

```

### Counts

```html
<button class="pf-v6-c-button pf-m-primary" type="button">
  <span class="pf-v6-c-button__text">View issues</span>
  <span class="pf-v6-c-button__count">
    <span class="pf-v6-c-badge pf-m-unread">
      7
      <span class="pf-v6-screen-reader">unread messages</span>
    </span>
  </span>
</button>
<button class="pf-v6-c-button pf-m-primary" type="button">
  <span class="pf-v6-c-button__text">View issues</span>
  <span class="pf-v6-c-button__count">
    <span class="pf-v6-c-badge pf-m-read">7</span>
  </span>
</button>
<button class="pf-v6-c-button pf-m-link" type="button">
  <span class="pf-v6-c-button__text">View issues</span>
  <span class="pf-v6-c-button__count">
    <span class="pf-v6-c-badge pf-m-unread">
      7
      <span class="pf-v6-screen-reader">unread messages</span>
    </span>
  </span>
</button>
<button class="pf-v6-c-button pf-m-link" type="button">
  <span class="pf-v6-c-button__text">View issues</span>
  <span class="pf-v6-c-button__count">
    <span class="pf-v6-c-badge pf-m-read">7</span>
  </span>
</button>
<br />
<strong>disabled</strong>
<br />
<button class="pf-v6-c-button pf-m-primary" type="button" disabled>
  <span class="pf-v6-c-button__text">View issues</span>
  <span class="pf-v6-c-button__count">
    <span class="pf-v6-c-badge pf-m-unread pf-m-disabled">7</span>
  </span>
</button>
<button class="pf-v6-c-button pf-m-primary" type="button" disabled>
  <span class="pf-v6-c-button__text">View issues</span>
  <span class="pf-v6-c-button__count">
    <span class="pf-v6-c-badge pf-m-read pf-m-disabled">7</span>
  </span>
</button>
<button class="pf-v6-c-button pf-m-link" type="button" disabled>
  <span class="pf-v6-c-button__text">View issues</span>
  <span class="pf-v6-c-button__count">
    <span class="pf-v6-c-badge pf-m-unread pf-m-disabled">7</span>
  </span>
</button>
<button class="pf-v6-c-button pf-m-link" type="button" disabled>
  <span class="pf-v6-c-button__text">View issues</span>
  <span class="pf-v6-c-button__count">
    <span class="pf-v6-c-badge pf-m-read pf-m-disabled">7</span>
  </span>
</button>

```

### Plain with no padding

```html
For when a plain/icon button is placed inline with text
<button
  class="pf-v6-c-button pf-m-no-padding pf-m-plain"
  type="button"
  aria-label="More info"
>
  <span class="pf-v6-c-button__icon">
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
        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
      />
    </svg>
  </span>
</button>
.

```

### Stateful

```html
<strong>Read</strong>
<br />
<button class="pf-v6-c-button pf-m-read pf-m-stateful" type="button">
  <span class="pf-v6-c-button__icon pf-m-start">
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
  </span>
  <span class="pf-v6-c-button__text">
    10
    <span class="pf-v6-screen-reader">items</span>
  </span>
</button>

<button
  class="pf-v6-c-button pf-m-read pf-m-stateful pf-m-clicked"
  type="button"
>
  <span class="pf-v6-c-button__icon pf-m-start">
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
  </span>
  <span class="pf-v6-c-button__text">
    10
    <span class="pf-v6-screen-reader">items</span>
  </span>
</button>

<br />
<br />

<strong>Unread</strong>
<br />
<button class="pf-v6-c-button pf-m-unread pf-m-stateful" type="button">
  <span class="pf-v6-c-button__icon pf-m-start">
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
  </span>
  <span class="pf-v6-c-button__text">
    10
    <span class="pf-v6-screen-reader">unread items</span>
  </span>
</button>

<button
  class="pf-v6-c-button pf-m-unread pf-m-stateful pf-m-clicked"
  type="button"
>
  <span class="pf-v6-c-button__icon pf-m-start">
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
  </span>
  <span class="pf-v6-c-button__text">
    10
    <span class="pf-v6-screen-reader">unread items</span>
  </span>
</button>

<br />
<br />

<strong>Attention</strong>
<br />
<button class="pf-v6-c-button pf-m-attention pf-m-stateful" type="button">
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M28 21c-1.103 0-2-.897-2-2v-4c0-4.884-3.523-8.955-8.159-9.823.405-.444.659-1.03.659-1.677C18.5 2.121 17.379 1 16 1s-2.5 1.121-2.5 2.5c0 .648.254 1.233.659 1.677C9.523 6.045 6 10.116 6 15v4c0 1.103-.897 2-2 2a1 1 0 0 0-1 1v3.5c0 .827.673 1.5 1.5 1.5H12c0 2.206 1.794 4 4 4s4-1.794 4-4h7.5c.827 0 1.5-.673 1.5-1.5V22a1 1 0 0 0-1-1ZM14.5 11a1.5 1.5 0 0 1 3 0v5a1.5 1.5 0 0 1-3 0v-5ZM16 24.014a2 2 0 1 1-.001-3.999A2 2 0 0 1 16 24.014Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">
    10
    <span class="pf-v6-screen-reader">unread items, needs attention</span>
  </span>
</button>

<button
  class="pf-v6-c-button pf-m-attention pf-m-stateful pf-m-clicked"
  type="button"
>
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M28 21c-1.103 0-2-.897-2-2v-4c0-4.884-3.523-8.955-8.159-9.823.405-.444.659-1.03.659-1.677C18.5 2.121 17.379 1 16 1s-2.5 1.121-2.5 2.5c0 .648.254 1.233.659 1.677C9.523 6.045 6 10.116 6 15v4c0 1.103-.897 2-2 2a1 1 0 0 0-1 1v3.5c0 .827.673 1.5 1.5 1.5H12c0 2.206 1.794 4 4 4s4-1.794 4-4h7.5c.827 0 1.5-.673 1.5-1.5V22a1 1 0 0 0-1-1ZM14.5 11a1.5 1.5 0 0 1 3 0v5a1.5 1.5 0 0 1-3 0v-5ZM16 24.014a2 2 0 1 1-.001-3.999A2 2 0 0 1 16 24.014Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">
    10
    <span class="pf-v6-screen-reader">unread items, needs attention</span>
  </span>
</button>

<br />
<br />

<strong>Plain</strong>
<br />
<button
  class="pf-v6-c-button pf-m-read pf-m-stateful pf-m-plain"
  type="button"
  aria-label="all items read"
>
  <span class="pf-v6-c-button__icon pf-m-start">
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
  </span>
</button>

<button
  class="pf-v6-c-button pf-m-read pf-m-stateful pf-m-clicked pf-m-plain"
  type="button"
  aria-label="all items read"
>
  <span class="pf-v6-c-button__icon pf-m-start">
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
  </span>
</button>

<br />

<button
  class="pf-v6-c-button pf-m-unread pf-m-stateful pf-m-plain"
  type="button"
  aria-label="unread items"
>
  <span class="pf-v6-c-button__icon pf-m-start">
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
  </span>
</button>

<button
  class="pf-v6-c-button pf-m-unread pf-m-stateful pf-m-clicked pf-m-plain"
  type="button"
  aria-label="unread items"
>
  <span class="pf-v6-c-button__icon pf-m-start">
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
  </span>
</button>

<br />

<button
  class="pf-v6-c-button pf-m-attention pf-m-stateful pf-m-plain"
  type="button"
  aria-label="unread items, needs attention"
>
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M28 21c-1.103 0-2-.897-2-2v-4c0-4.884-3.523-8.955-8.159-9.823.405-.444.659-1.03.659-1.677C18.5 2.121 17.379 1 16 1s-2.5 1.121-2.5 2.5c0 .648.254 1.233.659 1.677C9.523 6.045 6 10.116 6 15v4c0 1.103-.897 2-2 2a1 1 0 0 0-1 1v3.5c0 .827.673 1.5 1.5 1.5H12c0 2.206 1.794 4 4 4s4-1.794 4-4h7.5c.827 0 1.5-.673 1.5-1.5V22a1 1 0 0 0-1-1ZM14.5 11a1.5 1.5 0 0 1 3 0v5a1.5 1.5 0 0 1-3 0v-5ZM16 24.014a2 2 0 1 1-.001-3.999A2 2 0 0 1 16 24.014Z"
      />
    </svg>
  </span>
</button>

<button
  class="pf-v6-c-button pf-m-attention pf-m-stateful pf-m-clicked pf-m-plain"
  type="button"
  aria-label="unread items, needs attention"
>
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M28 21c-1.103 0-2-.897-2-2v-4c0-4.884-3.523-8.955-8.159-9.823.405-.444.659-1.03.659-1.677C18.5 2.121 17.379 1 16 1s-2.5 1.121-2.5 2.5c0 .648.254 1.233.659 1.677C9.523 6.045 6 10.116 6 15v4c0 1.103-.897 2-2 2a1 1 0 0 0-1 1v3.5c0 .827.673 1.5 1.5 1.5H12c0 2.206 1.794 4 4 4s4-1.794 4-4h7.5c.827 0 1.5-.673 1.5-1.5V22a1 1 0 0 0-1-1ZM14.5 11a1.5 1.5 0 0 1 3 0v5a1.5 1.5 0 0 1-3 0v-5ZM16 24.014a2 2 0 1 1-.001-3.999A2 2 0 0 1 16 24.014Z"
      />
    </svg>
  </span>
</button>

<br />
<br />

<strong>Plain with count</strong>
<br />
<button class="pf-v6-c-button pf-m-read pf-m-stateful pf-m-plain" type="button">
  <span class="pf-v6-c-button__icon pf-m-start">
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
  </span>
  <span class="pf-v6-c-button__text">
    10
    <span class="pf-v6-screen-reader">items</span>
  </span>
</button>

<button
  class="pf-v6-c-button pf-m-read pf-m-stateful pf-m-clicked pf-m-plain"
  type="button"
>
  <span class="pf-v6-c-button__icon pf-m-start">
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
  </span>
  <span class="pf-v6-c-button__text">
    10
    <span class="pf-v6-screen-reader">items</span>
  </span>
</button>

<br />

<button
  class="pf-v6-c-button pf-m-unread pf-m-stateful pf-m-plain"
  type="button"
>
  <span class="pf-v6-c-button__icon pf-m-start">
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
  </span>
  <span class="pf-v6-c-button__text">
    10
    <span class="pf-v6-screen-reader">unread items</span>
  </span>
</button>

<button
  class="pf-v6-c-button pf-m-unread pf-m-stateful pf-m-clicked pf-m-plain"
  type="button"
>
  <span class="pf-v6-c-button__icon pf-m-start">
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
  </span>
  <span class="pf-v6-c-button__text">
    10
    <span class="pf-v6-screen-reader">unread items</span>
  </span>
</button>

<br />

<button
  class="pf-v6-c-button pf-m-attention pf-m-stateful pf-m-plain"
  type="button"
>
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M28 21c-1.103 0-2-.897-2-2v-4c0-4.884-3.523-8.955-8.159-9.823.405-.444.659-1.03.659-1.677C18.5 2.121 17.379 1 16 1s-2.5 1.121-2.5 2.5c0 .648.254 1.233.659 1.677C9.523 6.045 6 10.116 6 15v4c0 1.103-.897 2-2 2a1 1 0 0 0-1 1v3.5c0 .827.673 1.5 1.5 1.5H12c0 2.206 1.794 4 4 4s4-1.794 4-4h7.5c.827 0 1.5-.673 1.5-1.5V22a1 1 0 0 0-1-1ZM14.5 11a1.5 1.5 0 0 1 3 0v5a1.5 1.5 0 0 1-3 0v-5ZM16 24.014a2 2 0 1 1-.001-3.999A2 2 0 0 1 16 24.014Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">
    10
    <span class="pf-v6-screen-reader">unread items, needs attention</span>
  </span>
</button>

<button
  class="pf-v6-c-button pf-m-attention pf-m-stateful pf-m-clicked pf-m-plain"
  type="button"
>
  <span class="pf-v6-c-button__icon pf-m-start">
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
        d="M28 21c-1.103 0-2-.897-2-2v-4c0-4.884-3.523-8.955-8.159-9.823.405-.444.659-1.03.659-1.677C18.5 2.121 17.379 1 16 1s-2.5 1.121-2.5 2.5c0 .648.254 1.233.659 1.677C9.523 6.045 6 10.116 6 15v4c0 1.103-.897 2-2 2a1 1 0 0 0-1 1v3.5c0 .827.673 1.5 1.5 1.5H12c0 2.206 1.794 4 4 4s4-1.794 4-4h7.5c.827 0 1.5-.673 1.5-1.5V22a1 1 0 0 0-1-1ZM14.5 11a1.5 1.5 0 0 1 3 0v5a1.5 1.5 0 0 1-3 0v-5ZM16 24.014a2 2 0 1 1-.001-3.999A2 2 0 0 1 16 24.014Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-button__text">
    10
    <span class="pf-v6-screen-reader">unread items, needs attention</span>
  </span>
</button>

```

### Favorite

A favorite button should use a plain button with the star icon. Applying `.pf-m-favorited` to the button initiates a microanimation and indicates that the item is favorited.

```html
<button
  class="pf-v6-c-button pf-m-favorite pf-m-plain"
  type="button"
  aria-label="not starred"
>
  <span class="pf-v6-c-button__icon">
    <span class="pf-v6-c-button__icon-favorite">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 576 512"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M528.1 171.5L382 150.2 316.7 17.8c-11.7-23.6-45.6-23.9-57.4 0L194 150.2 47.9 171.5c-26.2 3.8-36.7 36.1-17.7 54.6l105.7 103-25 145.5c-4.5 26.3 23.2 46 46.4 33.7L288 439.6l130.7 68.7c23.2 12.2 50.9-7.4 46.4-33.7l-25-145.5 105.7-103c19-18.5 8.5-50.8-17.7-54.6zM388.6 312.3l23.7 138.4L288 385.4l-124.3 65.3 23.7-138.4-100.6-98 139-20.2 62.2-126 62.2 126 139 20.2-100.6 98z"
        />
      </svg>
    </span>
    <span class="pf-v6-c-button__icon-favorited">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 576 512"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M259.3 17.8L194 150.2 47.9 171.5c-26.2 3.8-36.7 36.1-17.7 54.6l105.7 103-25 145.5c-4.5 26.3 23.2 46 46.4 33.7L288 439.6l130.7 68.7c23.2 12.2 50.9-7.4 46.4-33.7l-25-145.5 105.7-103c19-18.5 8.5-50.8-17.7-54.6L382 150.2 316.7 17.8c-11.7-23.6-45.6-23.9-57.4 0z"
        />
      </svg>
    </span>
  </span>
</button>
<button
  class="pf-v6-c-button pf-m-favorited pf-m-favorite pf-m-plain"
  type="button"
  aria-label="starred"
>
  <span class="pf-v6-c-button__icon">
    <span class="pf-v6-c-button__icon-favorite">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 576 512"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M528.1 171.5L382 150.2 316.7 17.8c-11.7-23.6-45.6-23.9-57.4 0L194 150.2 47.9 171.5c-26.2 3.8-36.7 36.1-17.7 54.6l105.7 103-25 145.5c-4.5 26.3 23.2 46 46.4 33.7L288 439.6l130.7 68.7c23.2 12.2 50.9-7.4 46.4-33.7l-25-145.5 105.7-103c19-18.5 8.5-50.8-17.7-54.6zM388.6 312.3l23.7 138.4L288 385.4l-124.3 65.3 23.7-138.4-100.6-98 139-20.2 62.2-126 62.2 126 139 20.2-100.6 98z"
        />
      </svg>
    </span>
    <span class="pf-v6-c-button__icon-favorited">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 576 512"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M259.3 17.8L194 150.2 47.9 171.5c-26.2 3.8-36.7 36.1-17.7 54.6l105.7 103-25 145.5c-4.5 26.3 23.2 46 46.4 33.7L288 439.6l130.7 68.7c23.2 12.2 50.9-7.4 46.4-33.7l-25-145.5 105.7-103c19-18.5 8.5-50.8-17.7-54.6L382 150.2 316.7 17.8c-11.7-23.6-45.6-23.9-57.4 0z"
        />
      </svg>
    </span>
  </span>
</button>

```

### Settings

```html
<button
  class="pf-v6-c-button pf-m-settings pf-m-plain"
  type="button"
  aria-label="Settings"
>
  <span class="pf-v6-c-button__icon">
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
        d="M30.168 12.894a.5.5 0 0 0-.488-.394h-2.732a11.512 11.512 0 0 0-.729-1.769l1.931-1.93a.5.5 0 0 0 .066-.625 14.693 14.693 0 0 0-4.393-4.392.498.498 0 0 0-.624.067l-1.93 1.93a11.512 11.512 0 0 0-1.769-.729V2.319a.5.5 0 0 0-.395-.489 14.81 14.81 0 0 0-6.211 0 .5.5 0 0 0-.395.489v2.733c-.614.196-1.207.439-1.769.729L8.8 3.851a.498.498 0 0 0-.624-.067 14.714 14.714 0 0 0-4.393 4.392.5.5 0 0 0 .066.625l1.931 1.93a11.512 11.512 0 0 0-.729 1.769H2.319a.5.5 0 0 0-.488.394 14.652 14.652 0 0 0 0 6.212.5.5 0 0 0 .488.394h2.732c.196.615.44 1.207.729 1.769l-1.931 1.93a.5.5 0 0 0-.066.625 14.673 14.673 0 0 0 4.393 4.392.498.498 0 0 0 .624-.067l1.93-1.93c.562.289 1.154.533 1.769.729v2.733a.5.5 0 0 0 .395.489 14.686 14.686 0 0 0 6.21 0 .5.5 0 0 0 .395-.489v-2.733a11.454 11.454 0 0 0 1.769-.729l1.93 1.93a.5.5 0 0 0 .624.067 14.714 14.714 0 0 0 4.393-4.392.5.5 0 0 0-.066-.625l-1.931-1.93c.289-.562.533-1.154.729-1.769h2.732a.5.5 0 0 0 .488-.394 14.652 14.652 0 0 0 0-6.212ZM16 21.25c-2.895 0-5.25-2.355-5.25-5.25s2.355-5.25 5.25-5.25 5.25 2.355 5.25 5.25-2.355 5.25-5.25 5.25Z"
      />
    </svg>
  </span>
</button>

```

### Hamburger

```html
<button
  class="pf-v6-c-button pf-m-hamburger pf-m-plain"
  type="button"
  aria-expanded="false"
  aria-label="Hamburger"
>
  <span class="pf-v6-c-button__icon">
    <svg
      viewBox="0 0 10 10"
      class="pf-v6-c-button--hamburger-icon pf-v6-svg"
      width="1em"
      height="1em"
    >
      <path class="pf-v6-c-button--hamburger-icon--top" d="M1,1 L9,1" />
      <path class="pf-v6-c-button--hamburger-icon--middle" d="M1,5 L9,5" />
      <path class="pf-v6-c-button--hamburger-icon--arrow" d="M1,5 L1,5 L1,5" />
      <path class="pf-v6-c-button--hamburger-icon--bottom" d="M9,9 L1,9" />
    </svg>
  </span>
</button>
<button
  class="pf-v6-c-button pf-m-expand pf-m-hamburger pf-m-plain"
  type="button"
  aria-expanded="false"
  aria-label="Hamburger"
>
  <span class="pf-v6-c-button__icon">
    <svg
      viewBox="0 0 10 10"
      class="pf-v6-c-button--hamburger-icon pf-v6-svg"
      width="1em"
      height="1em"
    >
      <path class="pf-v6-c-button--hamburger-icon--top" d="M1,1 L9,1" />
      <path class="pf-v6-c-button--hamburger-icon--middle" d="M1,5 L9,5" />
      <path class="pf-v6-c-button--hamburger-icon--arrow" d="M1,5 L1,5 L1,5" />
      <path class="pf-v6-c-button--hamburger-icon--bottom" d="M9,9 L1,9" />
    </svg>
  </span>
</button>
<button
  class="pf-v6-c-button pf-m-collapse pf-m-hamburger pf-m-plain"
  type="button"
  aria-expanded="true"
  aria-label="Hamburger"
>
  <span class="pf-v6-c-button__icon">
    <svg
      viewBox="0 0 10 10"
      class="pf-v6-c-button--hamburger-icon pf-v6-svg"
      width="1em"
      height="1em"
    >
      <path class="pf-v6-c-button--hamburger-icon--top" d="M1,1 L9,1" />
      <path class="pf-v6-c-button--hamburger-icon--middle" d="M1,5 L9,5" />
      <path class="pf-v6-c-button--hamburger-icon--arrow" d="M1,5 L1,5 L1,5" />
      <path class="pf-v6-c-button--hamburger-icon--bottom" d="M9,9 L1,9" />
    </svg>
  </span>
</button>

```

## Documentation

### Overview

Always add a modifier class to add color to the button.

### Button vs link

Semantic buttons and links are important for usability as well as accessibility. Using an `a` instead of a `button` element to perform user initiated actions should be avoided, unless absolutely necessary.

### Accessibility

| Attribute | Applied to | Outcome |
| -- | -- | -- |
| `aria-pressed="true or false"` | `.pf-v6-c-button` | Indicates that the button is a toggle. When set to true, `pf-m-active` should also be set so that the button displays in an active state. **Required when button is a toggle** |
| `aria-label="[button label text]"` | `.pf-v6-c-button.pf-m-plain` | Provides an accessible name for the button when an icon is used instead of text. **Required when icon is used with no supporting text** |
| `aria-label="[descriptive text]"` | `a.pf-v6-c-button`, `span.pf-v6-c-button.pf-m-link.pf-m-inline` | The button component's text should adequately describe its purpose. If it does not, `aria-label` can provide more detailed interaction information. |
| `disabled` | `button.pf-v6-c-button` | When a button element is used, indicates that it is unavailable and removes it from keyboard focus. **Required when button is disabled** |
| `aria-disabled=true` | `button.pf-v6-c-button` | When a button element is used, indicates that it is unavailable but does not prevent keyboard or hover interactions. Used when a disabled button provides interactive elements like a tooltip. |
| `aria-disabled=true` | `a.pf-v6-c-button.pf-m-disabled`, `span.pf-v6-c-button.pf-m-link.pf-m-inline.pf-m-disabled` | When a non-button element is used, indicates that it is unavailable. **Required when element is disabled** |
| `aria-expanded=true` | `.pf-v6-c-button.pf-m-expanded` | Indicates that the expanded content element is visible. **Required** |
| `tabindex="-1"` | `a.pf-v6-c-button.pf-m-disabled`, `span.pf-v6-c-button.pf-m-link.pf-m-inline.pf-m-disabled` | When a non-button element is used, removes it from keyboard focus. **Required when element is disabled** |
| `tabindex="0"` | `span.pf-v6-c-button.pf-m-link.pf-m-inline` | Inserts the span into the tab order of the page so that it is focusable. **Required when the element is a span** |

### Usage

| Class | Applied to | Outcome |
| -- | -- | -- |
| `.pf-v6-c-button` | `<button>, <span>` |  Initiates a button. Always use it with a modifier class. **Required** |
| `.pf-v6-c-button__icon` | `<span>` | Initiates a button icon. |
| `.pf-v6-c-button__progress` | `<span>` | Initiates a button progress container. |
| `.pf-v6-c-button__count` | `<span>` | Initiates a button count container. **Note:** Count should only be used on link buttons. |
| `.pf-m-primary` | `.pf-v6-c-button` | Modifies for primary styles. |
| `.pf-m-secondary` | `.pf-v6-c-button` | Modifies for secondary styles. |
| `.pf-m-tertiary` | `.pf-v6-c-button` | Modifies for tertiary styles. |
| `.pf-m-danger` | `.pf-v6-c-button` | Modifies for danger styles. |
| `.pf-m-warning` | `.pf-v6-c-button` | Modifies for warning styles. |
| `.pf-m-link` | `.pf-v6-c-button` | Modifies for link styles. This button has no background or border and is styled as a link. This button would commonly appear in a form and may include an icon. |
| `.pf-m-plain` | `.pf-v6-c-button` | Modifies for icon styles. This button has no background or border, uses a standard text color, and is used for `.pf-m-plain` icon buttons such as close, expand, kebab, stateful, etc. |
| `.pf-m-no-padding` | `.pf-v6-c-button.pf-m-plain` | Modifies a plain button to remove padding. This modifier should only be used when the button is inline within a sentence or block of text. Adjacent plain buttons without padding should always have spacing between them. |
| `.pf-m-inline` | `.pf-v6-c-button.pf-m-link` | Modifies for inline styles. This button is presented similar to a normal link and has no padding and is displayed inline with other inline content. When used as a `<span>`, the text will flow inline with text around it. |
| `.pf-m-block` | `.pf-v6-c-button` | Creates a block level button. |
| `.pf-m-control` | `.pf-v6-c-button` | Modifies for control styles. **Note:** This modifier should only be used when using buttons in the Input Group or Clipboard Copy components. |
| `.pf-m-expanded` | `.pf-v6-c-button.pf-m-control` | Modifies a control button for the expanded state. |
| `.pf-m-start` | `.pf-v6-c-button__icon` | Applies right spacing to an icon inside of a button when the icon comes before text. |
| `.pf-m-end` | `.pf-v6-c-button__icon` | Applies left spacing to an icon inside of a button when the icon comes after text. |
| `.pf-m-active` | `.pf-v6-c-button` | Forces display of the active state of the button. This modifier should be used when `aria-pressed` is set to true so that the button displays in an active state. |
| `.pf-m-small` | `.pf-v6-c-button` | Modifies the button for small/compact styles. |
| `.pf-m-aria-disabled` | `.pf-v6-c-button` | Modifies a button to be visually disabled, yet is still focusable. |
| `.pf-m-display-lg` | `.pf-v6-c-button`, `pf-v6-c-button.pf-m-link` | Modifies the button and link button for large display styling. For example, use this modifier to achieve "call to action" styles. |
| `.pf-m-progress` | `.pf-v6-c-button` | Indicates that the button supports the progress state. **Note:** Not used with the plain variation. |
| `.pf-m-in-progress` | `.pf-v6-c-button` | Indicates that the button is in the in progress state. |
| `.pf-m-stateful` | `.pf-v6-c-button` | Indicates that the button is used for one of read, unread, and attention states. **Note:** Always use with a modifier of `.pf-m-read`, `.pf-m-unread`, or `.pf-m-attention`. |
| `.pf-m-notify` | `.pf-v6-c-button` | Indicates that the button should show the user notification of an event. **Note:** This is intended for use with a bell icon in the notification badge. |
| `.pf-m-favorite` | `.pf-v6-c-button.pf-m-plain` | Modifies a plain button to be a favorite button. **Note:** This is intended for use with a star icon. |
| `.pf-m-favorited` | `.pf-v6-c-button.pf-m-plain.pf-m-favorite` | Modifies a favorite button to indicate that item is favorited. |
| `.pf-m-settings` | `.pf-v6-c-button.pf-m-plain` | Modifies a plain button to be a settings button. |
| `.pf-m-hamburger` | `.pf-v6-c-button.pf-m-plain` | Modifies a plain button to be a hamburger button. |
| `.pf-m-expand` | `.pf-v6-c-button.pf-m-hamburger` | Modifies a hamburger button to indicate that it will expand a menu. |
| `.pf-m-collapse` | `.pf-v6-c-button.pf-m-hamburger` | Modifies a hamburger button to indicate that it will collapse a menu. |
| `.pf-m-circle` | `.pf-v6-c-button` | Modifies a button to have a circular shape, instead of only rounded corners or a pill shape. Intended for buttons that contain only an icon. |
