---
id: Alert
section: components
cssPrefix: ['pf-v6-c-alert','pf-v6-c-alert-group']
---## Alert examples

### Types

```html
<div class="pf-v6-c-alert pf-m-custom" aria-label="Custom alert">
  <div class="pf-v6-c-alert__icon">
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
  <p class="pf-v6-c-alert__title">
    <span class="pf-v6-screen-reader">Custom alert:</span>
    Custom alert title
  </p>
</div>
<br />
<div class="pf-v6-c-alert pf-m-info" aria-label="Information alert">
  <div class="pf-v6-c-alert__icon">
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
  <p class="pf-v6-c-alert__title">
    <span class="pf-v6-screen-reader">Info alert:</span>
    Info alert title
  </p>
</div>
<br />
<div class="pf-v6-c-alert pf-m-success" aria-label="Success alert">
  <div class="pf-v6-c-alert__icon">
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
  <p class="pf-v6-c-alert__title">
    <span class="pf-v6-screen-reader">Success alert:</span>
    Success alert title
  </p>
</div>
<br />
<div class="pf-v6-c-alert pf-m-warning" aria-label="Warning alert">
  <div class="pf-v6-c-alert__icon">
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
  <p class="pf-v6-c-alert__title">
    <span class="pf-v6-screen-reader">Warning alert:</span>
    Warning alert title
  </p>
</div>
<br />
<div class="pf-v6-c-alert pf-m-danger" aria-label="Danger alert">
  <div class="pf-v6-c-alert__icon">
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
  <p class="pf-v6-c-alert__title">
    <span class="pf-v6-screen-reader">Danger alert:</span>
    Danger alert title
  </p>
</div>

```

### Variations

```html
<div class="pf-v6-c-alert pf-m-success" aria-label="Success alert">
  <div class="pf-v6-c-alert__icon">
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
  <p class="pf-v6-c-alert__title">
    <span class="pf-v6-screen-reader">Success alert:</span>
    Success alert title
  </p>
  <div class="pf-v6-c-alert__action">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Close success alert: Success alert title"
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
  </div>
  <div class="pf-v6-c-alert__description">
    <p>Success alert description. This should tell the user more information about the alert.</p>
  </div>
  <div class="pf-v6-c-alert__action-group">
    <button class="pf-v6-c-button pf-m-inline pf-m-link" type="button">
      <span class="pf-v6-c-button__text">View details</span>
    </button>
    <button class="pf-v6-c-button pf-m-inline pf-m-link" type="button">
      <span class="pf-v6-c-button__text">Ignore</span>
    </button>
  </div>
</div>
<br />
<div class="pf-v6-c-alert pf-m-success" aria-label="Success alert">
  <div class="pf-v6-c-alert__icon">
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
  <p class="pf-v6-c-alert__title">
    <span class="pf-v6-screen-reader">Success alert:</span>
    Success alert title
  </p>
  <div class="pf-v6-c-alert__action">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Close success alert: Success alert title"
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
  </div>
  <div class="pf-v6-c-alert__description">
    <p>
      Success alert description. This should tell the user more information about the alert.
      <a href="#">This is a link.</a>
    </p>
  </div>
</div>
<br />
<div class="pf-v6-c-alert pf-m-success" aria-label="Success alert">
  <div class="pf-v6-c-alert__icon">
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
  <p class="pf-v6-c-alert__title">
    <span class="pf-v6-screen-reader">Success alert:</span>
    Success alert title
  </p>
  <div class="pf-v6-c-alert__action">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Close success alert: Success alert title"
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
  </div>
  <div class="pf-v6-c-alert__action-group">
    <button class="pf-v6-c-button pf-m-inline pf-m-link" type="button">
      <span class="pf-v6-c-button__text">View details</span>
    </button>
    <button class="pf-v6-c-button pf-m-inline pf-m-link" type="button">
      <span class="pf-v6-c-button__text">Ignore</span>
    </button>
  </div>
</div>
<br />
<div class="pf-v6-c-alert pf-m-success" aria-label="Success alert">
  <div class="pf-v6-c-alert__icon">
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
  <p class="pf-v6-c-alert__title">
    <span class="pf-v6-screen-reader">Success alert:</span>
    Success alert title
  </p>
  <div class="pf-v6-c-alert__action">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Close success alert: Success alert title"
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
  </div>
</div>
<br />
<div class="pf-v6-c-alert pf-m-success" aria-label="Success alert">
  <div class="pf-v6-c-alert__icon">
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
  <p class="pf-v6-c-alert__title">
    <span class="pf-v6-screen-reader">Success alert:</span>
    Success alert title
  </p>
</div>
<br />
<div
  class="pf-v6-c-alert pf-m-success"
  aria-label="Success alert with title truncation"
>
  <div class="pf-v6-c-alert__icon">
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
  <p class="pf-v6-c-alert__title pf-m-truncate">
    <span class="pf-v6-screen-reader">Success alert:</span>
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur pellentesque neque cursus enim fringilla tincidunt. Proin lobortis aliquam dictum. Nam vel ullamcorper nulla, nec blandit dolor. Vivamus pellentesque neque justo, nec accumsan nulla rhoncus id. Suspendisse mollis, tortor quis faucibus volutpat, sem leo fringilla turpis, ac lacinia augue metus in nulla. Cras vestibulum lacinia orci. Pellentesque sodales consequat interdum. Sed porttitor tincidunt metus nec iaculis. Pellentesque non commodo justo. Morbi feugiat rhoncus neque, vitae facilisis diam aliquam nec. Sed dapibus vitae quam at tristique. Nunc vel commodo mi. Mauris et rhoncus leo.
  </p>
  <div class="pf-v6-c-alert__description">
    <p>This example uses ".pf-m-truncate" to limit the title to a single line and truncate any overflow text with ellipses.</p>
  </div>
</div>
<br />
<div
  class="pf-v6-c-alert pf-m-success"
  aria-label="Success alert with title truncation at 2 lines"
>
  <div class="pf-v6-c-alert__icon">
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
  <p
    class="pf-v6-c-alert__title pf-m-truncate"
    style="--pf-v6-c-alert__title--max-lines: 2"
  >
    <span class="pf-v6-screen-reader">Success alert:</span>
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur pellentesque neque cursus enim fringilla tincidunt. Proin lobortis aliquam dictum. Nam vel ullamcorper nulla, nec blandit dolor. Vivamus pellentesque neque justo, nec accumsan nulla rhoncus id. Suspendisse mollis, tortor quis faucibus volutpat, sem leo fringilla turpis, ac lacinia augue metus in nulla. Cras vestibulum lacinia orci. Pellentesque sodales consequat interdum. Sed porttitor tincidunt metus nec iaculis. Pellentesque non commodo justo. Morbi feugiat rhoncus neque, vitae facilisis diam aliquam nec. Sed dapibus vitae quam at tristique. Nunc vel commodo mi. Mauris et rhoncus leo.
  </p>
  <div class="pf-v6-c-alert__description">
    <p>This example uses ".pf-m-truncate" and sets "--pf-v6-c-alert__title--max-lines: 2" to limit title to two lines and truncate any overflow text with ellipses.</p>
  </div>
</div>

```

### Inline types

```html
<div
  class="pf-v6-c-alert pf-m-custom pf-m-inline"
  aria-label="Inline custom alert"
>
  <div class="pf-v6-c-alert__icon">
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
  <p class="pf-v6-c-alert__title">
    <span class="pf-v6-screen-reader">Custom inline alert:</span>
    Custom inline alert title
  </p>
</div>
<br />
<div
  class="pf-v6-c-alert pf-m-info pf-m-inline"
  aria-label="Inline information alert"
>
  <div class="pf-v6-c-alert__icon">
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
  <p class="pf-v6-c-alert__title">
    <span class="pf-v6-screen-reader">Info alert:</span>
    Info inline alert title
  </p>
</div>
<br />
<div
  class="pf-v6-c-alert pf-m-success pf-m-inline"
  aria-label="Inline success alert"
>
  <div class="pf-v6-c-alert__icon">
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
  <p class="pf-v6-c-alert__title">
    <span class="pf-v6-screen-reader">Success alert:</span>
    Success inline alert title
  </p>
</div>
<br />
<div
  class="pf-v6-c-alert pf-m-warning pf-m-inline"
  aria-label="Inline warning alert"
>
  <div class="pf-v6-c-alert__icon">
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
  <p class="pf-v6-c-alert__title">
    <span class="pf-v6-screen-reader">Warning alert:</span>
    Warning inline alert title
  </p>
</div>
<br />
<div
  class="pf-v6-c-alert pf-m-danger pf-m-inline"
  aria-label="Inline danger alert"
>
  <div class="pf-v6-c-alert__icon">
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
  <p class="pf-v6-c-alert__title">
    <span class="pf-v6-screen-reader">Danger alert:</span>
    Danger inline alert title
  </p>
</div>

```

### Inline variations

```html
<div class="pf-v6-c-alert pf-m-success pf-m-inline" aria-label="Success alert">
  <div class="pf-v6-c-alert__icon">
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
  <p class="pf-v6-c-alert__title">
    <span class="pf-v6-screen-reader">Success alert:</span>
    Success alert title
  </p>
  <div class="pf-v6-c-alert__action">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Close success alert: Success alert title"
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
  </div>
  <div class="pf-v6-c-alert__description">
    <p>Success alert description. This should tell the user more information about the alert.</p>
  </div>
  <div class="pf-v6-c-alert__action-group">
    <button class="pf-v6-c-button pf-m-inline pf-m-link" type="button">
      <span class="pf-v6-c-button__text">View details</span>
    </button>
    <button class="pf-v6-c-button pf-m-inline pf-m-link" type="button">
      <span class="pf-v6-c-button__text">Ignore</span>
    </button>
  </div>
</div>
<br />
<div class="pf-v6-c-alert pf-m-success pf-m-inline" aria-label="Success alert">
  <div class="pf-v6-c-alert__icon">
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
  <p class="pf-v6-c-alert__title">
    <span class="pf-v6-screen-reader">Success alert:</span>
    Success alert title
  </p>
  <div class="pf-v6-c-alert__action">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Close success alert: Success alert title"
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
  </div>
  <div class="pf-v6-c-alert__description">
    <p>
      Success alert description. This should tell the user more information about the alert.
      <a href="#">This is a link.</a>
    </p>
  </div>
</div>
<br />
<div class="pf-v6-c-alert pf-m-success pf-m-inline" aria-label="Success alert">
  <div class="pf-v6-c-alert__icon">
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
  <p class="pf-v6-c-alert__title">
    <span class="pf-v6-screen-reader">Success alert:</span>
    Success alert title
  </p>
  <div class="pf-v6-c-alert__action">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Close success alert: Success alert title"
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
  </div>
  <div class="pf-v6-c-alert__action-group">
    <button class="pf-v6-c-button pf-m-inline pf-m-link" type="button">
      <span class="pf-v6-c-button__text">View details</span>
    </button>
    <button class="pf-v6-c-button pf-m-inline pf-m-link" type="button">
      <span class="pf-v6-c-button__text">Ignore</span>
    </button>
  </div>
</div>
<br />
<div class="pf-v6-c-alert pf-m-success pf-m-inline" aria-label="Success alert">
  <div class="pf-v6-c-alert__icon">
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
  <p class="pf-v6-c-alert__title">
    <span class="pf-v6-screen-reader">Success alert:</span>
    Success alert title
  </p>
</div>

```

### Custom icon

```html
<div class="pf-v6-c-alert pf-m-success" aria-label="Success alert">
  <div class="pf-v6-c-alert__icon">
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
  </div>
  <p class="pf-v6-c-alert__title">
    <span class="pf-v6-screen-reader">Success alert:</span>
    Success alert title
  </p>
</div>
<br />
<div class="pf-v6-c-alert pf-m-success pf-m-inline" aria-label="Success alert">
  <div class="pf-v6-c-alert__icon">
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
  </div>
  <p class="pf-v6-c-alert__title">
    <span class="pf-v6-screen-reader">Success alert:</span>
    Success alert title (inline)
  </p>
</div>

```

### Inline plain

```html
<div
  class="pf-v6-c-alert pf-m-success pf-m-plain pf-m-inline"
  aria-label="Success alert"
>
  <div class="pf-v6-c-alert__icon">
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
  <p class="pf-v6-c-alert__title">
    <span class="pf-v6-screen-reader">Success alert:</span>
    Success alert title
  </p>
</div>

```

### Expandable

```html
<div
  class="pf-v6-c-alert pf-m-expandable pf-m-success"
  aria-label="Success alert"
>
  <div class="pf-v6-c-alert__toggle">
    <button
      class="pf-v6-c-button pf-m-plain"
      id="alert-expandable-example-1-toggle"
      type="button"
      aria-expanded="false"
      aria-labelledby="alert-expandable-example-1-title alert-expandable-example-1-toggle"
      aria-label="Details"
    >
      <span class="pf-v6-c-button__icon">
        <span class="pf-v6-c-alert__toggle-icon">
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
              d="M18.71 5.29a.996.996 0 0 0-1.41 0l-7.29 7.29-7.3-7.29a.987.987 0 0 0-1.41-.02.987.987 0 0 0-.02 1.41l.02.02 7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65a.996.996 0 0 0 0-1.41Z"
            />
          </svg>
        </span>
      </span>
    </button>
  </div>
  <div class="pf-v6-c-alert__icon">
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
  <p class="pf-v6-c-alert__title" id="alert-expandable-example-1-title">
    <span class="pf-v6-screen-reader">Success alert:</span>
    Success alert title
  </p>
  <div class="pf-v6-c-alert__action">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Close success alert: Success alert title"
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
  </div>
  <div class="pf-v6-c-alert__description" hidden>
    <p>Success alert description. This should tell the user more information about the alert.</p>
  </div>
  <div class="pf-v6-c-alert__action-group">
    <button class="pf-v6-c-button pf-m-inline pf-m-link" type="button">
      <span class="pf-v6-c-button__text">View details</span>
    </button>
    <button class="pf-v6-c-button pf-m-inline pf-m-link" type="button">
      <span class="pf-v6-c-button__text">Ignore</span>
    </button>
  </div>
</div>
<br />
<div
  class="pf-v6-c-alert pf-m-expandable pf-m-expanded pf-m-success"
  aria-label="Success alert"
>
  <div class="pf-v6-c-alert__toggle">
    <button
      class="pf-v6-c-button pf-m-plain"
      id="alert-expandable-example-2-toggle"
      type="button"
      aria-expanded="true"
      aria-labelledby="alert-expandable-example-2-title alert-expandable-example-2-toggle"
      aria-label="Details"
    >
      <span class="pf-v6-c-button__icon">
        <span class="pf-v6-c-alert__toggle-icon">
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
              d="M18.71 5.29a.996.996 0 0 0-1.41 0l-7.29 7.29-7.3-7.29a.987.987 0 0 0-1.41-.02.987.987 0 0 0-.02 1.41l.02.02 7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65a.996.996 0 0 0 0-1.41Z"
            />
          </svg>
        </span>
      </span>
    </button>
  </div>
  <div class="pf-v6-c-alert__icon">
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
  <p class="pf-v6-c-alert__title" id="alert-expandable-example-2-title">
    <span class="pf-v6-screen-reader">Success alert:</span>
    Success alert title (expanded)
  </p>
  <div class="pf-v6-c-alert__action">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Close success alert: Success alert title"
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
  </div>
  <div class="pf-v6-c-alert__description">
    <p>Success alert description. This should tell the user more information about the alert.</p>
  </div>
  <div class="pf-v6-c-alert__action-group">
    <button class="pf-v6-c-button pf-m-inline pf-m-link" type="button">
      <span class="pf-v6-c-button__text">View details</span>
    </button>
    <button class="pf-v6-c-button pf-m-inline pf-m-link" type="button">
      <span class="pf-v6-c-button__text">Ignore</span>
    </button>
  </div>
</div>
<br />
<div
  class="pf-v6-c-alert pf-m-expandable pf-m-success pf-m-inline"
  aria-label="Success alert"
>
  <div class="pf-v6-c-alert__toggle">
    <button
      class="pf-v6-c-button pf-m-plain"
      id="alert-expandable-example-3-toggle"
      type="button"
      aria-expanded="false"
      aria-labelledby="alert-expandable-example-3-title alert-expandable-example-3-toggle"
      aria-label="Details"
    >
      <span class="pf-v6-c-button__icon">
        <span class="pf-v6-c-alert__toggle-icon">
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
              d="M18.71 5.29a.996.996 0 0 0-1.41 0l-7.29 7.29-7.3-7.29a.987.987 0 0 0-1.41-.02.987.987 0 0 0-.02 1.41l.02.02 7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65a.996.996 0 0 0 0-1.41Z"
            />
          </svg>
        </span>
      </span>
    </button>
  </div>
  <div class="pf-v6-c-alert__icon">
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
  <p class="pf-v6-c-alert__title" id="alert-expandable-example-3-title">
    <span class="pf-v6-screen-reader">Success alert:</span>
    Success alert title
  </p>
  <div class="pf-v6-c-alert__action">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Close success alert: Success alert title"
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
  </div>
  <div class="pf-v6-c-alert__description" hidden>
    <p>Success alert description. This should tell the user more information about the alert.</p>
  </div>
  <div class="pf-v6-c-alert__action-group">
    <button class="pf-v6-c-button pf-m-inline pf-m-link" type="button">
      <span class="pf-v6-c-button__text">View details</span>
    </button>
    <button class="pf-v6-c-button pf-m-inline pf-m-link" type="button">
      <span class="pf-v6-c-button__text">Ignore</span>
    </button>
  </div>
</div>
<br />
<div
  class="pf-v6-c-alert pf-m-expandable pf-m-expanded pf-m-success pf-m-inline"
  aria-label="Success alert"
>
  <div class="pf-v6-c-alert__toggle">
    <button
      class="pf-v6-c-button pf-m-plain"
      id="alert-expandable-example-4-toggle"
      type="button"
      aria-expanded="true"
      aria-labelledby="alert-expandable-example-4-title alert-expandable-example-4-toggle"
      aria-label="Details"
    >
      <span class="pf-v6-c-button__icon">
        <span class="pf-v6-c-alert__toggle-icon">
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
              d="M18.71 5.29a.996.996 0 0 0-1.41 0l-7.29 7.29-7.3-7.29a.987.987 0 0 0-1.41-.02.987.987 0 0 0-.02 1.41l.02.02 7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65a.996.996 0 0 0 0-1.41Z"
            />
          </svg>
        </span>
      </span>
    </button>
  </div>
  <div class="pf-v6-c-alert__icon">
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
  <p class="pf-v6-c-alert__title" id="alert-expandable-example-4-title">
    <span class="pf-v6-screen-reader">Success alert:</span>
    Success alert title (expanded)
  </p>
  <div class="pf-v6-c-alert__action">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Close success alert: Success alert title"
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
  </div>
  <div class="pf-v6-c-alert__description">
    <p>Success alert description. This should tell the user more information about the alert.</p>
  </div>
  <div class="pf-v6-c-alert__action-group">
    <button class="pf-v6-c-button pf-m-inline pf-m-link" type="button">
      <span class="pf-v6-c-button__text">View details</span>
    </button>
    <button class="pf-v6-c-button pf-m-inline pf-m-link" type="button">
      <span class="pf-v6-c-button__text">Ignore</span>
    </button>
  </div>
</div>

```

## Alert group examples

### Static alert group

An alert group is optional when only one static alert is needed. It becomes required when more than one alert is used in a list.

```html
<ul class="pf-v6-c-alert-group" role="list">
  <li class="pf-v6-c-alert-group__item">
    <div
      class="pf-v6-c-alert pf-m-inline pf-m-success"
      aria-label="Success alert"
    >
      <div class="pf-v6-c-alert__icon">
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
      <p class="pf-v6-c-alert__title">
        <span class="pf-v6-screen-reader">Success alert:</span>
        Success alert title
      </p>
    </div>
  </li>

  <li class="pf-v6-c-alert-group__item">
    <div
      class="pf-v6-c-alert pf-m-inline pf-m-danger"
      aria-label="Danger alert"
    >
      <div class="pf-v6-c-alert__icon">
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
      <p class="pf-v6-c-alert__title">
        <span class="pf-v6-screen-reader">Danger alert:</span>
        Danger alert title
      </p>
    </div>
  </li>

  <li class="pf-v6-c-alert-group__item">
    <div
      class="pf-v6-c-alert pf-m-inline pf-m-info"
      aria-label="Information alert"
    >
      <div class="pf-v6-c-alert__icon">
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
      <p class="pf-v6-c-alert__title">
        <span class="pf-v6-screen-reader">Info alert:</span>
        Info alert title
      </p>
      <div class="pf-v6-c-alert__description">
        <p>
          Info alert description.
          <a href="#">This is a link.</a>
        </p>
      </div>
    </div>
  </li>
</ul>

```

### Toast alert group

An alert group is required to display toast alerts. An alert group that includes the `.pf-m-toast` modifier becomes a toast alert group with unique positioning in the top-right corner of the window.

Every toast alert must include a close button to dismiss the alert.

When toast alerts include a link or action, these elements are not announced as interactive elements by screen readers. Whenever you include a link or button, incorporate it into the message so that it’s clear to the user how to access the same contents or action without clicking the link or button directly in the toast. For example, if your toast alert displays a message “The build is complete. Go to the Builds page to download,” the screen reader user is given instructions on how to find their build for download.

For sighted users, interactive elements can be included in this message in one of the following ways:

* Using a link to the Builds page: "The build is complete. Go to the [Builds](#) page to download" using `<a href="#">Builds</a>`
* Using a button to download: "The build is complete. Go to the Builds page to <button class="pf-v6-c-button pf-m-link pf-m-inline" type="button">download</button>" using `<button class="pf-v6-c-button pf-m-link pf-m-inline type="button">download</button>`

```html isFullscreen
<ul class="pf-v6-c-alert-group pf-m-toast" role="list">
  <li class="pf-v6-c-alert-group__item">
    <div class="pf-v6-c-alert pf-m-success" aria-label="Success toast alert">
      <div class="pf-v6-c-alert__icon">
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
      <p class="pf-v6-c-alert__title" id="alert_one_title">
        <span class="pf-v6-screen-reader">Success alert:</span>
        Success toast alert title
      </p>
      <div class="pf-v6-c-alert__description">
        <p>
          Info toast alert description. From the settings tab, click
          <a href="#">View logs</a>&nbsp;to review the details.
        </p>
      </div>
      <div class="pf-v6-c-alert__action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close success alert: Success alert title"
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
      </div>
    </div>
  </li>

  <li class="pf-v6-c-alert-group__item">
    <div class="pf-v6-c-alert pf-m-danger" aria-label="Danger toast alert">
      <div class="pf-v6-c-alert__icon">
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
      <p class="pf-v6-c-alert__title" id="alert_two_title">
        <span class="pf-v6-screen-reader">Danger alert:</span>
        Danger toast alert title
      </p>
      <div class="pf-v6-c-alert__action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close danger alert: Danger alert title"
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
      </div>
    </div>
  </li>

  <li class="pf-v6-c-alert-group__item">
    <div class="pf-v6-c-alert pf-m-info" aria-label="Information toast alert">
      <div class="pf-v6-c-alert__icon">
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
      <p class="pf-v6-c-alert__title" id="alert_three_title">
        <span class="pf-v6-screen-reader">Info alert:</span>
        Info toast alert title
      </p>
      <div class="pf-v6-c-alert__description">
        <p>
          Info toast alert description. From the settings tab, click
          <a href="#">View logs</a>&nbsp;to review the details.
        </p>
      </div>
      <div class="pf-v6-c-alert__action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close info alert: Info alert title"
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
      </div>
    </div>
  </li>
  <li>
    <button
      class="pf-v6-c-alert-group__overflow-button"
    >View 3 more notifications</button>
  </li>
</ul>

```

## Documentation

### Alert overview

Add a modifier class to the default alert to change the color: `.pf-m-success`, `.pf-m-danger`, `.pf-m-warning`, or `.pf-m-info`.

### Alert usage

| Class | Applied to | Outcome |
| -- | -- | -- |
| `.pf-v6-c-alert` | `<div>` | Initiates the alert component. Always use with a status modifier class. **Required** |
| `.pf-v6-c-alert__toggle` | `<div>` | Defines the expandable alert toggle icon. **Required for expandable alerts** |
| `.pf-v6-c-alert__toggle-icon` | `<span>` | Defines the expandable alert toggle icon. **Required for expandable alerts** |
| `.pf-v6-c-alert__icon` | `<div>` | Defines the alert icon. **Required** |
| `.pf-v6-c-alert__title` | `<p>, <h1-h6>` | Defines the alert title. **Required** |
| `.pf-v6-c-alert__description` | `<div>` | Defines the alert description area. |
| `.pf-v6-c-alert__action` | `<div>` | Defines the action button wrapper. Should contain `.pf-v6-c-button.pf-m-plain` for close action or `.pf-v6-c-button.pf-m-link` for link text. It should only include one action. |
| `.pf-v6-c-alert__action-group` | `<div>` | Defines the action button group. Should contain `.pf-v6-c-button.pf-m-link.pf-m-inline` for inline link text. **Note:** only inline link buttons are supported in the alert action group. |
| `.pf-m-custom` | `.pf-v6-c-alert` | Applies custom status styling. |
| `.pf-m-success` | `.pf-v6-c-alert` | Applies success status styling. |
| `.pf-m-danger` | `.pf-v6-c-alert` | Applies danger status styling. |
| `.pf-m-warning` | `.pf-v6-c-alert` | Applies warning status styling. |
| `.pf-m-info` | `.pf-v6-c-alert` | Applies info status styling. |
| `.pf-m-inline` | `.pf-v6-c-alert` | Applies inline styling. |
| `.pf-m-plain` | `.pf-v6-c-alert.pf-m-inline` | Applies plain styling to an inline alert. |
| `.pf-m-expandable` | `.pf-v6-c-alert` | Applies expandable styles to the alert. |
| `.pf-m-expanded` | `.pf-v6-c-alert.pf-m-expandable` | Applies expanded styles to an expandable alert. |
| `.pf-m-truncate` | `.pf-v6-c-alert__title` | Modifies the title to display a single line and truncate any overflow text with ellipses. **Note:** you can specify the max number of lines to show by setting the `--pf-v6-c-alert__title--max-lines` (the default value is `1`). |

### Alert group overview

The alert component is used to contain and align consecutive alerts.  Alert groups can either be embedded alongside a page's content or in the top-right corner as a toast group using the `.pf-m-toast` modifier.

### Alert group usage

| Class | Applied to | Outcome |
| -- | -- | -- |
| `.pf-v6-c-alert-group` | `<ul>` | Creates an alert group component. **Required** |
| `.pf-v6-c-alert-group__item` | `<li>` | Creates an alert group item. **Required** |
| `.pf-v6-c-alert-group__overflow-button` | `<button>` | Applies overflow button styling to an alert group overflow button. |
| `.pf-m-toast`| `.pf-v6-c-alert-group` | Applies toast alert styling to an alert group. |
