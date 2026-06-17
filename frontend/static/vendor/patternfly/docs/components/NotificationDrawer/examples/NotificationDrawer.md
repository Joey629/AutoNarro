---
id: Notification drawer
section: components
cssPrefix: pf-v6-c-notification-drawer
---## Examples

### Basic

```html
<div class="pf-v6-c-notification-drawer">
  <div class="pf-v6-c-notification-drawer__header">
    <h1 class="pf-v6-c-notification-drawer__header-title">Notifications</h1>
    <span class="pf-v6-c-notification-drawer__header-status">3 unread</span>
    <div class="pf-v6-c-notification-drawer__header-action">
      <button
        class="pf-v6-c-menu-toggle pf-m-plain"
        type="button"
        aria-expanded="false"
        aria-label="Menu toggle"
        id="notification-drawer-basic-example-menu-toggle"
      >
        <span class="pf-v6-c-menu-toggle__icon">
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
              d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
            />
          </svg>
        </span>
      </button>
      <div class="pf-v6-c-notification-drawer__header-action-close">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close"
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
  </div>
  <div class="pf-v6-c-notification-drawer__body">
    <ul class="pf-v6-c-notification-drawer__list" role="list">
      <li
        class="pf-v6-c-notification-drawer__list-item pf-m-hoverable pf-m-info"
        tabindex="0"
      >
        <div class="pf-v6-c-notification-drawer__list-item-header">
          <span class="pf-v6-c-notification-drawer__list-item-header-icon">
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
          </span>
          <h2 class="pf-v6-c-notification-drawer__list-item-header-title">
            <span class="pf-v6-screen-reader">Info notification:</span>
            Unread
            info notification title
          </h2>
        </div>
        <div class="pf-v6-c-notification-drawer__list-item-action">
          <button
            class="pf-v6-c-menu-toggle pf-m-plain"
            type="button"
            aria-expanded="false"
            aria-label="Menu toggle"
            id="notification-drawer-basic-example-menu-toggle-1"
          >
            <span class="pf-v6-c-menu-toggle__icon">
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
                  d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                />
              </svg>
            </span>
          </button>
        </div>
        <div
          class="pf-v6-c-notification-drawer__list-item-description"
        >This is an info notification description.</div>
        <div
          class="pf-v6-c-notification-drawer__list-item-timestamp"
        >5 minutes ago</div>
      </li>

      <li
        class="pf-v6-c-notification-drawer__list-item pf-m-hoverable pf-m-custom"
        tabindex="0"
      >
        <div class="pf-v6-c-notification-drawer__list-item-header">
          <span class="pf-v6-c-notification-drawer__list-item-header-icon">
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
          <h2 class="pf-v6-c-notification-drawer__list-item-header-title">
            <span class="pf-v6-screen-reader">Custom notification:</span>
            Unread
            recommendation notification title. This is a long title to show how the title will wrap if it is long and wraps to multiple lines.
          </h2>
        </div>
        <div class="pf-v6-c-notification-drawer__list-item-action">
          <button
            class="pf-v6-c-menu-toggle pf-m-plain"
            type="button"
            aria-expanded="false"
            aria-label="Menu toggle"
            id="notification-drawer-basic-example-menu-toggle-3"
          >
            <span class="pf-v6-c-menu-toggle__icon">
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
                  d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                />
              </svg>
            </span>
          </button>
        </div>
        <div
          class="pf-v6-c-notification-drawer__list-item-description"
        >This is a recommendation notification description. This is a long description to show how the title will wrap if it is long and wraps to multiple lines.</div>
        <div
          class="pf-v6-c-notification-drawer__list-item-timestamp"
        >10 minutes ago</div>
      </li>

      <li
        class="pf-v6-c-notification-drawer__list-item pf-m-hoverable pf-m-custom"
        tabindex="0"
      >
        <div class="pf-v6-c-notification-drawer__list-item-header">
          <span class="pf-v6-c-notification-drawer__list-item-header-icon">
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
          <h2 class="pf-v6-c-notification-drawer__list-item-header-title">
            <span class="pf-v6-screen-reader">Custom notification:</span>
            Unread
            recommendation notification title. This is a long title to show how the title will wrap if it is long and wraps to multiple lines.
          </h2>
        </div>
        <div class="pf-v6-c-notification-drawer__list-item-action">
          <button
            class="pf-v6-c-menu-toggle pf-m-plain"
            type="button"
            aria-expanded="false"
            aria-label="Menu toggle"
            id="notification-drawer-basic-example-menu-toggle-4"
          >
            <span class="pf-v6-c-menu-toggle__icon">
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
                  d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                />
              </svg>
            </span>
          </button>
        </div>
        <div
          class="pf-v6-c-notification-drawer__list-item-description"
        >This is a recommendation notification description. This is a long description to show how the title will wrap if it is long and wraps to multiple lines.</div>
        <div
          class="pf-v6-c-notification-drawer__list-item-timestamp"
        >20 minutes ago</div>
      </li>
      <li
        class="pf-v6-c-notification-drawer__list-item pf-m-read pf-m-warning pf-m-hoverable"
      >
        <div class="pf-v6-c-notification-drawer__list-item-header">
          <span class="pf-v6-c-notification-drawer__list-item-header-icon">
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
          </span>
          <h2 class="pf-v6-c-notification-drawer__list-item-header-title">
            <span class="pf-v6-screen-reader">Warning notification:</span>
            Read warning notification title
          </h2>
        </div>
        <div class="pf-v6-c-notification-drawer__list-item-action">
          <button
            class="pf-v6-c-menu-toggle pf-m-plain"
            type="button"
            aria-expanded="false"
            aria-label="Menu toggle"
            id="notification-drawer-basic-example-menu-toggle-5"
          >
            <span class="pf-v6-c-menu-toggle__icon">
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
                  d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                />
              </svg>
            </span>
          </button>
        </div>
        <div
          class="pf-v6-c-notification-drawer__list-item-description"
        >This is a warning notification description.</div>
        <div
          class="pf-v6-c-notification-drawer__list-item-timestamp"
        >20 minutes ago</div>
      </li>
      <li
        class="pf-v6-c-notification-drawer__list-item pf-m-read pf-m-success pf-m-hoverable"
      >
        <div class="pf-v6-c-notification-drawer__list-item-header">
          <span class="pf-v6-c-notification-drawer__list-item-header-icon">
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
          </span>
          <h2 class="pf-v6-c-notification-drawer__list-item-header-title">
            <span class="pf-v6-screen-reader">Success notification:</span>
            Read success notification title
          </h2>
        </div>
        <div class="pf-v6-c-notification-drawer__list-item-action">
          <button
            class="pf-v6-c-menu-toggle pf-m-plain"
            type="button"
            aria-expanded="false"
            aria-label="Menu toggle"
            id="notification-drawer-basic-example-menu-toggle-6"
          >
            <span class="pf-v6-c-menu-toggle__icon">
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
                  d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                />
              </svg>
            </span>
          </button>
        </div>
        <div
          class="pf-v6-c-notification-drawer__list-item-description"
        >This is a success notification description.</div>
        <div
          class="pf-v6-c-notification-drawer__list-item-timestamp"
        >30 minutes ago</div>
      </li>
      <li
        class="pf-v6-c-notification-drawer__list-item pf-m-read pf-m-success pf-m-hoverable"
      >
        <div class="pf-v6-c-notification-drawer__list-item-header">
          <span class="pf-v6-c-notification-drawer__list-item-header-icon">
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
          </span>
          <h2
            class="pf-v6-c-notification-drawer__list-item-header-title pf-m-truncate"
          >
            <span class="pf-v6-screen-reader">Success notification:</span>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent quis odio risus. Ut dictum vitae sapien at posuere. Nullam suscipit massa quis lacus pellentesque scelerisque. Donec non maximus neque, quis ornare nunc. Vivamus in nibh sed libero feugiat feugiat. Nulla lacinia rutrum est, a commodo odio vestibulum suscipit. Nullam id quam et quam porttitor interdum quis nec tellus. Vestibulum arcu dui, pulvinar eu tellus in, semper mattis diam. Sed commodo tincidunt lacus non pulvinar. Curabitur tempor molestie vestibulum. Vivamus vel mi dignissim, efficitur neque eget, efficitur massa. Mauris vitae nunc augue. Donec augue lorem, malesuada et quam vitae, volutpat mattis nisi. Nullam nec venenatis ex, quis lobortis purus. Sed nisl dolor, mattis sit amet tincidunt quis, mollis sed massa.
          </h2>
        </div>
        <div class="pf-v6-c-notification-drawer__list-item-action">
          <button
            class="pf-v6-c-menu-toggle pf-m-plain"
            type="button"
            aria-expanded="false"
            aria-label="Menu toggle"
            id="notification-drawer-basic-example-menu-toggle-7"
          >
            <span class="pf-v6-c-menu-toggle__icon">
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
                  d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                />
              </svg>
            </span>
          </button>
        </div>
        <div
          class="pf-v6-c-notification-drawer__list-item-description"
        >This example uses ".pf-m-truncate" to limit the title to a single line and truncate any overflow text with ellipses.</div>
        <div
          class="pf-v6-c-notification-drawer__list-item-timestamp"
        >40 minutes ago</div>
      </li>
      <li
        class="pf-v6-c-notification-drawer__list-item pf-m-read pf-m-success pf-m-hoverable"
      >
        <div class="pf-v6-c-notification-drawer__list-item-header">
          <span class="pf-v6-c-notification-drawer__list-item-header-icon">
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
          </span>
          <h2
            class="pf-v6-c-notification-drawer__list-item-header-title pf-m-truncate"
            style="--pf-v6-c-notification-drawer__list-item-header-title--max-lines: 2"
          >
            <span class="pf-v6-screen-reader">Success notification:</span>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent quis odio risus. Ut dictum vitae sapien at posuere. Nullam suscipit massa quis lacus pellentesque scelerisque. Donec non maximus neque, quis ornare nunc. Vivamus in nibh sed libero feugiat feugiat. Nulla lacinia rutrum est, a commodo odio vestibulum suscipit. Nullam id quam et quam porttitor interdum quis nec tellus. Vestibulum arcu dui, pulvinar eu tellus in, semper mattis diam. Sed commodo tincidunt lacus non pulvinar. Curabitur tempor molestie vestibulum. Vivamus vel mi dignissim, efficitur neque eget, efficitur massa. Mauris vitae nunc augue. Donec augue lorem, malesuada et quam vitae, volutpat mattis nisi. Nullam nec venenatis ex, quis lobortis purus. Sed nisl dolor, mattis sit amet tincidunt quis, mollis sed massa.
          </h2>
        </div>
        <div class="pf-v6-c-notification-drawer__list-item-action">
          <button
            class="pf-v6-c-menu-toggle pf-m-plain"
            type="button"
            aria-expanded="false"
            aria-label="Menu toggle"
            id="notification-drawer-basic-example-menu-toggle-8"
          >
            <span class="pf-v6-c-menu-toggle__icon">
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
                  d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                />
              </svg>
            </span>
          </button>
        </div>
        <div
          class="pf-v6-c-notification-drawer__list-item-description"
        >This example uses ".pf-m-truncate" and sets "--pf-v6-c-notification-drawer__list-item-header-title--max-lines: 2" to limit title to two lines and truncate any overflow text with ellipses.</div>
        <div
          class="pf-v6-c-notification-drawer__list-item-timestamp"
        >50 minutes ago</div>
      </li>
      <li class="pf-v6-c-notification-drawer__list-item pf-m-read pf-m-success">
        <div class="pf-v6-c-notification-drawer__list-item-header">
          <span class="pf-v6-c-notification-drawer__list-item-header-icon">
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
          </span>
          <h2 class="pf-v6-c-notification-drawer__list-item-header-title">
            <span class="pf-v6-screen-reader">Success notification:</span>
            Notification drawer item title
          </h2>
        </div>
        <div
          class="pf-v6-c-notification-drawer__list-item-action pf-m-no-offset"
        >
          <button class="pf-v6-c-button pf-m-primary" type="button">
            <span class="pf-v6-c-button__text">Action</span>
          </button>
        </div>
        <div
          class="pf-v6-c-notification-drawer__list-item-description"
        >This example uses ".pf-m-no-offset" on the action wrapper to disable the default offset for button alignment.</div>
        <div
          class="pf-v6-c-notification-drawer__list-item-timestamp"
        >55 minutes ago</div>
      </li>
    </ul>
  </div>
</div>

```

### Groups

```html
<div class="pf-v6-c-notification-drawer">
  <div class="pf-v6-c-notification-drawer__header">
    <h1 class="pf-v6-c-notification-drawer__header-title">Notifications</h1>
    <span class="pf-v6-c-notification-drawer__header-status">9 unread</span>
    <div class="pf-v6-c-notification-drawer__header-action">
      <button
        class="pf-v6-c-menu-toggle pf-m-plain"
        type="button"
        aria-expanded="false"
        aria-label="Menu toggle"
        id="notification-drawer-groups-example-menu-toggle"
      >
        <span class="pf-v6-c-menu-toggle__icon">
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
              d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
            />
          </svg>
        </span>
      </button>
      <div class="pf-v6-c-notification-drawer__header-action-close">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close"
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
  </div>
  <div class="pf-v6-c-notification-drawer__body">
    <div class="pf-v6-c-notification-drawer__group-list">
      <section class="pf-v6-c-notification-drawer__group">
        <h1>
          <button
            class="pf-v6-c-notification-drawer__group-toggle"
            aria-expanded="false"
          >
            <div
              class="pf-v6-c-notification-drawer__group-toggle-title"
            >First notification group</div>
            <div class="pf-v6-c-notification-drawer__group-toggle-count">
              <span class="pf-v6-c-badge pf-m-unread">2</span>
            </div>
            <span class="pf-v6-c-notification-drawer__group-toggle-icon">
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
          </button>
        </h1>
        <ul class="pf-v6-c-notification-drawer__list" role="list" hidden>
          <li
            class="pf-v6-c-notification-drawer__list-item pf-m-hoverable pf-m-info"
            tabindex="0"
          >
            <div class="pf-v6-c-notification-drawer__list-item-header">
              <span class="pf-v6-c-notification-drawer__list-item-header-icon">
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
              </span>
              <h2 class="pf-v6-c-notification-drawer__list-item-header-title">
                <span class="pf-v6-screen-reader">Info notification:</span>
                Unread
                info notification title
              </h2>
            </div>
            <div class="pf-v6-c-notification-drawer__list-item-action">
              <button
                class="pf-v6-c-menu-toggle pf-m-plain"
                type="button"
                aria-expanded="false"
                aria-label="Menu toggle"
                id="notification-drawer-groups-example-group1-menu-toggle-1"
              >
                <span class="pf-v6-c-menu-toggle__icon">
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
                      d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                    />
                  </svg>
                </span>
              </button>
            </div>
            <div
              class="pf-v6-c-notification-drawer__list-item-description"
            >This is an info notification description.</div>
            <div
              class="pf-v6-c-notification-drawer__list-item-timestamp"
            >5 minutes ago</div>
          </li>

          <li
            class="pf-v6-c-notification-drawer__list-item pf-m-hoverable pf-m-custom"
            tabindex="0"
          >
            <div class="pf-v6-c-notification-drawer__list-item-header">
              <span class="pf-v6-c-notification-drawer__list-item-header-icon">
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
              <h2 class="pf-v6-c-notification-drawer__list-item-header-title">
                <span class="pf-v6-screen-reader">Custom notification:</span>
                Unread
                recommendation notification title. This is a long title to show how the title will wrap if it is long and wraps to multiple lines.
              </h2>
            </div>
            <div class="pf-v6-c-notification-drawer__list-item-action">
              <button
                class="pf-v6-c-menu-toggle pf-m-plain"
                type="button"
                aria-expanded="false"
                aria-label="Menu toggle"
                id="notification-drawer-groups-example-group1-menu-toggle-3"
              >
                <span class="pf-v6-c-menu-toggle__icon">
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
                      d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                    />
                  </svg>
                </span>
              </button>
            </div>
            <div
              class="pf-v6-c-notification-drawer__list-item-description"
            >This is a recommendation notification description. This is a long description to show how the title will wrap if it is long and wraps to multiple lines.</div>
            <div
              class="pf-v6-c-notification-drawer__list-item-timestamp"
            >10 minutes ago</div>
          </li>

          <li
            class="pf-v6-c-notification-drawer__list-item pf-m-hoverable pf-m-custom"
            tabindex="0"
          >
            <div class="pf-v6-c-notification-drawer__list-item-header">
              <span class="pf-v6-c-notification-drawer__list-item-header-icon">
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
              <h2 class="pf-v6-c-notification-drawer__list-item-header-title">
                <span class="pf-v6-screen-reader">Custom notification:</span>
                Unread
                recommendation notification title. This is a long title to show how the title will wrap if it is long and wraps to multiple lines.
              </h2>
            </div>
            <div class="pf-v6-c-notification-drawer__list-item-action">
              <button
                class="pf-v6-c-menu-toggle pf-m-plain"
                type="button"
                aria-expanded="false"
                aria-label="Menu toggle"
                id="notification-drawer-groups-example-group1-menu-toggle-4"
              >
                <span class="pf-v6-c-menu-toggle__icon">
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
                      d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                    />
                  </svg>
                </span>
              </button>
            </div>
            <div
              class="pf-v6-c-notification-drawer__list-item-description"
            >This is a recommendation notification description. This is a long description to show how the title will wrap if it is long and wraps to multiple lines.</div>
            <div
              class="pf-v6-c-notification-drawer__list-item-timestamp"
            >20 minutes ago</div>
          </li>
          <li
            class="pf-v6-c-notification-drawer__list-item pf-m-read pf-m-warning pf-m-hoverable"
          >
            <div class="pf-v6-c-notification-drawer__list-item-header">
              <span class="pf-v6-c-notification-drawer__list-item-header-icon">
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
              </span>
              <h2 class="pf-v6-c-notification-drawer__list-item-header-title">
                <span class="pf-v6-screen-reader">Warning notification:</span>
                Read warning notification title
              </h2>
            </div>
            <div class="pf-v6-c-notification-drawer__list-item-action">
              <button
                class="pf-v6-c-menu-toggle pf-m-plain"
                type="button"
                aria-expanded="false"
                aria-label="Menu toggle"
                id="notification-drawer-groups-example-group1-menu-toggle-5"
              >
                <span class="pf-v6-c-menu-toggle__icon">
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
                      d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                    />
                  </svg>
                </span>
              </button>
            </div>
            <div
              class="pf-v6-c-notification-drawer__list-item-description"
            >This is a warning notification description.</div>
            <div
              class="pf-v6-c-notification-drawer__list-item-timestamp"
            >20 minutes ago</div>
          </li>
          <li
            class="pf-v6-c-notification-drawer__list-item pf-m-read pf-m-success pf-m-hoverable"
          >
            <div class="pf-v6-c-notification-drawer__list-item-header">
              <span class="pf-v6-c-notification-drawer__list-item-header-icon">
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
              </span>
              <h2 class="pf-v6-c-notification-drawer__list-item-header-title">
                <span class="pf-v6-screen-reader">Success notification:</span>
                Read success notification title
              </h2>
            </div>
            <div class="pf-v6-c-notification-drawer__list-item-action">
              <button
                class="pf-v6-c-menu-toggle pf-m-plain"
                type="button"
                aria-expanded="false"
                aria-label="Menu toggle"
                id="notification-drawer-groups-example-group1-menu-toggle-6"
              >
                <span class="pf-v6-c-menu-toggle__icon">
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
                      d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                    />
                  </svg>
                </span>
              </button>
            </div>
            <div
              class="pf-v6-c-notification-drawer__list-item-description"
            >This is a success notification description.</div>
            <div
              class="pf-v6-c-notification-drawer__list-item-timestamp"
            >30 minutes ago</div>
          </li>
          <li
            class="pf-v6-c-notification-drawer__list-item pf-m-read pf-m-success pf-m-hoverable"
          >
            <div class="pf-v6-c-notification-drawer__list-item-header">
              <span class="pf-v6-c-notification-drawer__list-item-header-icon">
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
              </span>
              <h2
                class="pf-v6-c-notification-drawer__list-item-header-title pf-m-truncate"
              >
                <span class="pf-v6-screen-reader">Success notification:</span>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent quis odio risus. Ut dictum vitae sapien at posuere. Nullam suscipit massa quis lacus pellentesque scelerisque. Donec non maximus neque, quis ornare nunc. Vivamus in nibh sed libero feugiat feugiat. Nulla lacinia rutrum est, a commodo odio vestibulum suscipit. Nullam id quam et quam porttitor interdum quis nec tellus. Vestibulum arcu dui, pulvinar eu tellus in, semper mattis diam. Sed commodo tincidunt lacus non pulvinar. Curabitur tempor molestie vestibulum. Vivamus vel mi dignissim, efficitur neque eget, efficitur massa. Mauris vitae nunc augue. Donec augue lorem, malesuada et quam vitae, volutpat mattis nisi. Nullam nec venenatis ex, quis lobortis purus. Sed nisl dolor, mattis sit amet tincidunt quis, mollis sed massa.
              </h2>
            </div>
            <div class="pf-v6-c-notification-drawer__list-item-action">
              <button
                class="pf-v6-c-menu-toggle pf-m-plain"
                type="button"
                aria-expanded="false"
                aria-label="Menu toggle"
                id="notification-drawer-groups-example-group1-menu-toggle-7"
              >
                <span class="pf-v6-c-menu-toggle__icon">
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
                      d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                    />
                  </svg>
                </span>
              </button>
            </div>
            <div
              class="pf-v6-c-notification-drawer__list-item-description"
            >This example uses ".pf-m-truncate" to limit the title to a single line and truncate any overflow text with ellipses.</div>
            <div
              class="pf-v6-c-notification-drawer__list-item-timestamp"
            >40 minutes ago</div>
          </li>
          <li
            class="pf-v6-c-notification-drawer__list-item pf-m-read pf-m-success pf-m-hoverable"
          >
            <div class="pf-v6-c-notification-drawer__list-item-header">
              <span class="pf-v6-c-notification-drawer__list-item-header-icon">
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
              </span>
              <h2
                class="pf-v6-c-notification-drawer__list-item-header-title pf-m-truncate"
                style="--pf-v6-c-notification-drawer__list-item-header-title--max-lines: 2"
              >
                <span class="pf-v6-screen-reader">Success notification:</span>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent quis odio risus. Ut dictum vitae sapien at posuere. Nullam suscipit massa quis lacus pellentesque scelerisque. Donec non maximus neque, quis ornare nunc. Vivamus in nibh sed libero feugiat feugiat. Nulla lacinia rutrum est, a commodo odio vestibulum suscipit. Nullam id quam et quam porttitor interdum quis nec tellus. Vestibulum arcu dui, pulvinar eu tellus in, semper mattis diam. Sed commodo tincidunt lacus non pulvinar. Curabitur tempor molestie vestibulum. Vivamus vel mi dignissim, efficitur neque eget, efficitur massa. Mauris vitae nunc augue. Donec augue lorem, malesuada et quam vitae, volutpat mattis nisi. Nullam nec venenatis ex, quis lobortis purus. Sed nisl dolor, mattis sit amet tincidunt quis, mollis sed massa.
              </h2>
            </div>
            <div class="pf-v6-c-notification-drawer__list-item-action">
              <button
                class="pf-v6-c-menu-toggle pf-m-plain"
                type="button"
                aria-expanded="false"
                aria-label="Menu toggle"
                id="notification-drawer-groups-example-group1-menu-toggle-8"
              >
                <span class="pf-v6-c-menu-toggle__icon">
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
                      d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                    />
                  </svg>
                </span>
              </button>
            </div>
            <div
              class="pf-v6-c-notification-drawer__list-item-description"
            >This example uses ".pf-m-truncate" and sets "--pf-v6-c-notification-drawer__list-item-header-title--max-lines: 2" to limit title to two lines and truncate any overflow text with ellipses.</div>
            <div
              class="pf-v6-c-notification-drawer__list-item-timestamp"
            >50 minutes ago</div>
          </li>
          <li
            class="pf-v6-c-notification-drawer__list-item pf-m-read pf-m-success"
          >
            <div class="pf-v6-c-notification-drawer__list-item-header">
              <span class="pf-v6-c-notification-drawer__list-item-header-icon">
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
              </span>
              <h2 class="pf-v6-c-notification-drawer__list-item-header-title">
                <span class="pf-v6-screen-reader">Success notification:</span>
                Notification drawer item title
              </h2>
            </div>
            <div
              class="pf-v6-c-notification-drawer__list-item-action pf-m-no-offset"
            >
              <button class="pf-v6-c-button pf-m-primary" type="button">
                <span class="pf-v6-c-button__text">Action</span>
              </button>
            </div>
            <div
              class="pf-v6-c-notification-drawer__list-item-description"
            >This example uses ".pf-m-no-offset" on the action wrapper to disable the default offset for button alignment.</div>
            <div
              class="pf-v6-c-notification-drawer__list-item-timestamp"
            >55 minutes ago</div>
          </li>
        </ul>
      </section>
      <section class="pf-v6-c-notification-drawer__group pf-m-expanded">
        <h1>
          <button
            class="pf-v6-c-notification-drawer__group-toggle"
            aria-expanded="true"
          >
            <div
              class="pf-v6-c-notification-drawer__group-toggle-title"
            >Second notification group</div>
            <div class="pf-v6-c-notification-drawer__group-toggle-count">
              <span class="pf-v6-c-badge pf-m-unread">2</span>
            </div>
            <span class="pf-v6-c-notification-drawer__group-toggle-icon">
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
          </button>
        </h1>
        <ul class="pf-v6-c-notification-drawer__list" role="list">
          <li
            class="pf-v6-c-notification-drawer__list-item pf-m-hoverable pf-m-info"
            tabindex="0"
          >
            <div class="pf-v6-c-notification-drawer__list-item-header">
              <span class="pf-v6-c-notification-drawer__list-item-header-icon">
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
              </span>
              <h2 class="pf-v6-c-notification-drawer__list-item-header-title">
                <span class="pf-v6-screen-reader">Info notification:</span>
                Unread
                info notification title
              </h2>
            </div>
            <div class="pf-v6-c-notification-drawer__list-item-action">
              <button
                class="pf-v6-c-menu-toggle pf-m-plain"
                type="button"
                aria-expanded="false"
                aria-label="Menu toggle"
                id="notification-drawer-groups-example-group2-menu-toggle-1"
              >
                <span class="pf-v6-c-menu-toggle__icon">
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
                      d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                    />
                  </svg>
                </span>
              </button>
            </div>
            <div
              class="pf-v6-c-notification-drawer__list-item-description"
            >This is an info notification description.</div>
            <div
              class="pf-v6-c-notification-drawer__list-item-timestamp"
            >5 minutes ago</div>
          </li>

          <li
            class="pf-v6-c-notification-drawer__list-item pf-m-hoverable pf-m-custom"
            tabindex="0"
          >
            <div class="pf-v6-c-notification-drawer__list-item-header">
              <span class="pf-v6-c-notification-drawer__list-item-header-icon">
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
              <h2 class="pf-v6-c-notification-drawer__list-item-header-title">
                <span class="pf-v6-screen-reader">Custom notification:</span>
                Unread
                recommendation notification title. This is a long title to show how the title will wrap if it is long and wraps to multiple lines.
              </h2>
            </div>
            <div class="pf-v6-c-notification-drawer__list-item-action">
              <button
                class="pf-v6-c-menu-toggle pf-m-plain"
                type="button"
                aria-expanded="false"
                aria-label="Menu toggle"
                id="notification-drawer-groups-example-group2-menu-toggle-3"
              >
                <span class="pf-v6-c-menu-toggle__icon">
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
                      d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                    />
                  </svg>
                </span>
              </button>
            </div>
            <div
              class="pf-v6-c-notification-drawer__list-item-description"
            >This is a recommendation notification description. This is a long description to show how the title will wrap if it is long and wraps to multiple lines.</div>
            <div
              class="pf-v6-c-notification-drawer__list-item-timestamp"
            >10 minutes ago</div>
          </li>

          <li
            class="pf-v6-c-notification-drawer__list-item pf-m-hoverable pf-m-custom"
            tabindex="0"
          >
            <div class="pf-v6-c-notification-drawer__list-item-header">
              <span class="pf-v6-c-notification-drawer__list-item-header-icon">
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
              <h2 class="pf-v6-c-notification-drawer__list-item-header-title">
                <span class="pf-v6-screen-reader">Custom notification:</span>
                Unread
                recommendation notification title. This is a long title to show how the title will wrap if it is long and wraps to multiple lines.
              </h2>
            </div>
            <div class="pf-v6-c-notification-drawer__list-item-action">
              <button
                class="pf-v6-c-menu-toggle pf-m-plain"
                type="button"
                aria-expanded="false"
                aria-label="Menu toggle"
                id="notification-drawer-groups-example-group2-menu-toggle-4"
              >
                <span class="pf-v6-c-menu-toggle__icon">
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
                      d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                    />
                  </svg>
                </span>
              </button>
            </div>
            <div
              class="pf-v6-c-notification-drawer__list-item-description"
            >This is a recommendation notification description. This is a long description to show how the title will wrap if it is long and wraps to multiple lines.</div>
            <div
              class="pf-v6-c-notification-drawer__list-item-timestamp"
            >20 minutes ago</div>
          </li>
          <li
            class="pf-v6-c-notification-drawer__list-item pf-m-read pf-m-warning pf-m-hoverable"
          >
            <div class="pf-v6-c-notification-drawer__list-item-header">
              <span class="pf-v6-c-notification-drawer__list-item-header-icon">
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
              </span>
              <h2 class="pf-v6-c-notification-drawer__list-item-header-title">
                <span class="pf-v6-screen-reader">Warning notification:</span>
                Read warning notification title
              </h2>
            </div>
            <div class="pf-v6-c-notification-drawer__list-item-action">
              <button
                class="pf-v6-c-menu-toggle pf-m-plain"
                type="button"
                aria-expanded="false"
                aria-label="Menu toggle"
                id="notification-drawer-groups-example-group2-menu-toggle-5"
              >
                <span class="pf-v6-c-menu-toggle__icon">
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
                      d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                    />
                  </svg>
                </span>
              </button>
            </div>
            <div
              class="pf-v6-c-notification-drawer__list-item-description"
            >This is a warning notification description.</div>
            <div
              class="pf-v6-c-notification-drawer__list-item-timestamp"
            >20 minutes ago</div>
          </li>
          <li
            class="pf-v6-c-notification-drawer__list-item pf-m-read pf-m-success pf-m-hoverable"
          >
            <div class="pf-v6-c-notification-drawer__list-item-header">
              <span class="pf-v6-c-notification-drawer__list-item-header-icon">
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
              </span>
              <h2 class="pf-v6-c-notification-drawer__list-item-header-title">
                <span class="pf-v6-screen-reader">Success notification:</span>
                Read success notification title
              </h2>
            </div>
            <div class="pf-v6-c-notification-drawer__list-item-action">
              <button
                class="pf-v6-c-menu-toggle pf-m-plain"
                type="button"
                aria-expanded="false"
                aria-label="Menu toggle"
                id="notification-drawer-groups-example-group2-menu-toggle-6"
              >
                <span class="pf-v6-c-menu-toggle__icon">
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
                      d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                    />
                  </svg>
                </span>
              </button>
            </div>
            <div
              class="pf-v6-c-notification-drawer__list-item-description"
            >This is a success notification description.</div>
            <div
              class="pf-v6-c-notification-drawer__list-item-timestamp"
            >30 minutes ago</div>
          </li>
          <li
            class="pf-v6-c-notification-drawer__list-item pf-m-read pf-m-success pf-m-hoverable"
          >
            <div class="pf-v6-c-notification-drawer__list-item-header">
              <span class="pf-v6-c-notification-drawer__list-item-header-icon">
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
              </span>
              <h2
                class="pf-v6-c-notification-drawer__list-item-header-title pf-m-truncate"
              >
                <span class="pf-v6-screen-reader">Success notification:</span>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent quis odio risus. Ut dictum vitae sapien at posuere. Nullam suscipit massa quis lacus pellentesque scelerisque. Donec non maximus neque, quis ornare nunc. Vivamus in nibh sed libero feugiat feugiat. Nulla lacinia rutrum est, a commodo odio vestibulum suscipit. Nullam id quam et quam porttitor interdum quis nec tellus. Vestibulum arcu dui, pulvinar eu tellus in, semper mattis diam. Sed commodo tincidunt lacus non pulvinar. Curabitur tempor molestie vestibulum. Vivamus vel mi dignissim, efficitur neque eget, efficitur massa. Mauris vitae nunc augue. Donec augue lorem, malesuada et quam vitae, volutpat mattis nisi. Nullam nec venenatis ex, quis lobortis purus. Sed nisl dolor, mattis sit amet tincidunt quis, mollis sed massa.
              </h2>
            </div>
            <div class="pf-v6-c-notification-drawer__list-item-action">
              <button
                class="pf-v6-c-menu-toggle pf-m-plain"
                type="button"
                aria-expanded="false"
                aria-label="Menu toggle"
                id="notification-drawer-groups-example-group2-menu-toggle-7"
              >
                <span class="pf-v6-c-menu-toggle__icon">
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
                      d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                    />
                  </svg>
                </span>
              </button>
            </div>
            <div
              class="pf-v6-c-notification-drawer__list-item-description"
            >This example uses ".pf-m-truncate" to limit the title to a single line and truncate any overflow text with ellipses.</div>
            <div
              class="pf-v6-c-notification-drawer__list-item-timestamp"
            >40 minutes ago</div>
          </li>
          <li
            class="pf-v6-c-notification-drawer__list-item pf-m-read pf-m-success pf-m-hoverable"
          >
            <div class="pf-v6-c-notification-drawer__list-item-header">
              <span class="pf-v6-c-notification-drawer__list-item-header-icon">
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
              </span>
              <h2
                class="pf-v6-c-notification-drawer__list-item-header-title pf-m-truncate"
                style="--pf-v6-c-notification-drawer__list-item-header-title--max-lines: 2"
              >
                <span class="pf-v6-screen-reader">Success notification:</span>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent quis odio risus. Ut dictum vitae sapien at posuere. Nullam suscipit massa quis lacus pellentesque scelerisque. Donec non maximus neque, quis ornare nunc. Vivamus in nibh sed libero feugiat feugiat. Nulla lacinia rutrum est, a commodo odio vestibulum suscipit. Nullam id quam et quam porttitor interdum quis nec tellus. Vestibulum arcu dui, pulvinar eu tellus in, semper mattis diam. Sed commodo tincidunt lacus non pulvinar. Curabitur tempor molestie vestibulum. Vivamus vel mi dignissim, efficitur neque eget, efficitur massa. Mauris vitae nunc augue. Donec augue lorem, malesuada et quam vitae, volutpat mattis nisi. Nullam nec venenatis ex, quis lobortis purus. Sed nisl dolor, mattis sit amet tincidunt quis, mollis sed massa.
              </h2>
            </div>
            <div class="pf-v6-c-notification-drawer__list-item-action">
              <button
                class="pf-v6-c-menu-toggle pf-m-plain"
                type="button"
                aria-expanded="false"
                aria-label="Menu toggle"
                id="notification-drawer-groups-example-group2-menu-toggle-8"
              >
                <span class="pf-v6-c-menu-toggle__icon">
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
                      d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                    />
                  </svg>
                </span>
              </button>
            </div>
            <div
              class="pf-v6-c-notification-drawer__list-item-description"
            >This example uses ".pf-m-truncate" and sets "--pf-v6-c-notification-drawer__list-item-header-title--max-lines: 2" to limit title to two lines and truncate any overflow text with ellipses.</div>
            <div
              class="pf-v6-c-notification-drawer__list-item-timestamp"
            >50 minutes ago</div>
          </li>
          <li
            class="pf-v6-c-notification-drawer__list-item pf-m-read pf-m-success"
          >
            <div class="pf-v6-c-notification-drawer__list-item-header">
              <span class="pf-v6-c-notification-drawer__list-item-header-icon">
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
              </span>
              <h2 class="pf-v6-c-notification-drawer__list-item-header-title">
                <span class="pf-v6-screen-reader">Success notification:</span>
                Notification drawer item title
              </h2>
            </div>
            <div
              class="pf-v6-c-notification-drawer__list-item-action pf-m-no-offset"
            >
              <button class="pf-v6-c-button pf-m-primary" type="button">
                <span class="pf-v6-c-button__text">Action</span>
              </button>
            </div>
            <div
              class="pf-v6-c-notification-drawer__list-item-description"
            >This example uses ".pf-m-no-offset" on the action wrapper to disable the default offset for button alignment.</div>
            <div
              class="pf-v6-c-notification-drawer__list-item-timestamp"
            >55 minutes ago</div>
          </li>
        </ul>
      </section>
      <section class="pf-v6-c-notification-drawer__group">
        <h1>
          <button
            class="pf-v6-c-notification-drawer__group-toggle"
            aria-expanded="false"
          >
            <div
              class="pf-v6-c-notification-drawer__group-toggle-title"
            >Third notification group</div>
            <div class="pf-v6-c-notification-drawer__group-toggle-count">
              <span class="pf-v6-c-badge pf-m-unread">3</span>
            </div>
            <span class="pf-v6-c-notification-drawer__group-toggle-icon">
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
          </button>
        </h1>
        <ul class="pf-v6-c-notification-drawer__list" role="list" hidden>
          <li
            class="pf-v6-c-notification-drawer__list-item pf-m-hoverable pf-m-info"
            tabindex="0"
          >
            <div class="pf-v6-c-notification-drawer__list-item-header">
              <span class="pf-v6-c-notification-drawer__list-item-header-icon">
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
              </span>
              <h2 class="pf-v6-c-notification-drawer__list-item-header-title">
                <span class="pf-v6-screen-reader">Info notification:</span>
                Unread
                info notification title
              </h2>
            </div>
            <div class="pf-v6-c-notification-drawer__list-item-action">
              <button
                class="pf-v6-c-menu-toggle pf-m-plain"
                type="button"
                aria-expanded="false"
                aria-label="Menu toggle"
                id="notification-drawer-groups-example-group3-menu-toggle-1"
              >
                <span class="pf-v6-c-menu-toggle__icon">
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
                      d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                    />
                  </svg>
                </span>
              </button>
            </div>
            <div
              class="pf-v6-c-notification-drawer__list-item-description"
            >This is an info notification description.</div>
            <div
              class="pf-v6-c-notification-drawer__list-item-timestamp"
            >5 minutes ago</div>
          </li>

          <li
            class="pf-v6-c-notification-drawer__list-item pf-m-hoverable pf-m-custom"
            tabindex="0"
          >
            <div class="pf-v6-c-notification-drawer__list-item-header">
              <span class="pf-v6-c-notification-drawer__list-item-header-icon">
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
              <h2 class="pf-v6-c-notification-drawer__list-item-header-title">
                <span class="pf-v6-screen-reader">Custom notification:</span>
                Unread
                recommendation notification title. This is a long title to show how the title will wrap if it is long and wraps to multiple lines.
              </h2>
            </div>
            <div class="pf-v6-c-notification-drawer__list-item-action">
              <button
                class="pf-v6-c-menu-toggle pf-m-plain"
                type="button"
                aria-expanded="false"
                aria-label="Menu toggle"
                id="notification-drawer-groups-example-group3-menu-toggle-3"
              >
                <span class="pf-v6-c-menu-toggle__icon">
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
                      d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                    />
                  </svg>
                </span>
              </button>
            </div>
            <div
              class="pf-v6-c-notification-drawer__list-item-description"
            >This is a recommendation notification description. This is a long description to show how the title will wrap if it is long and wraps to multiple lines.</div>
            <div
              class="pf-v6-c-notification-drawer__list-item-timestamp"
            >10 minutes ago</div>
          </li>

          <li
            class="pf-v6-c-notification-drawer__list-item pf-m-hoverable pf-m-custom"
            tabindex="0"
          >
            <div class="pf-v6-c-notification-drawer__list-item-header">
              <span class="pf-v6-c-notification-drawer__list-item-header-icon">
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
              <h2 class="pf-v6-c-notification-drawer__list-item-header-title">
                <span class="pf-v6-screen-reader">Custom notification:</span>
                Unread
                recommendation notification title. This is a long title to show how the title will wrap if it is long and wraps to multiple lines.
              </h2>
            </div>
            <div class="pf-v6-c-notification-drawer__list-item-action">
              <button
                class="pf-v6-c-menu-toggle pf-m-plain"
                type="button"
                aria-expanded="false"
                aria-label="Menu toggle"
                id="notification-drawer-groups-example-group3-menu-toggle-4"
              >
                <span class="pf-v6-c-menu-toggle__icon">
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
                      d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                    />
                  </svg>
                </span>
              </button>
            </div>
            <div
              class="pf-v6-c-notification-drawer__list-item-description"
            >This is a recommendation notification description. This is a long description to show how the title will wrap if it is long and wraps to multiple lines.</div>
            <div
              class="pf-v6-c-notification-drawer__list-item-timestamp"
            >20 minutes ago</div>
          </li>
          <li
            class="pf-v6-c-notification-drawer__list-item pf-m-read pf-m-warning pf-m-hoverable"
          >
            <div class="pf-v6-c-notification-drawer__list-item-header">
              <span class="pf-v6-c-notification-drawer__list-item-header-icon">
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
              </span>
              <h2 class="pf-v6-c-notification-drawer__list-item-header-title">
                <span class="pf-v6-screen-reader">Warning notification:</span>
                Read warning notification title
              </h2>
            </div>
            <div class="pf-v6-c-notification-drawer__list-item-action">
              <button
                class="pf-v6-c-menu-toggle pf-m-plain"
                type="button"
                aria-expanded="false"
                aria-label="Menu toggle"
                id="notification-drawer-groups-example-group3-menu-toggle-5"
              >
                <span class="pf-v6-c-menu-toggle__icon">
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
                      d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                    />
                  </svg>
                </span>
              </button>
            </div>
            <div
              class="pf-v6-c-notification-drawer__list-item-description"
            >This is a warning notification description.</div>
            <div
              class="pf-v6-c-notification-drawer__list-item-timestamp"
            >20 minutes ago</div>
          </li>
          <li
            class="pf-v6-c-notification-drawer__list-item pf-m-read pf-m-success pf-m-hoverable"
          >
            <div class="pf-v6-c-notification-drawer__list-item-header">
              <span class="pf-v6-c-notification-drawer__list-item-header-icon">
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
              </span>
              <h2 class="pf-v6-c-notification-drawer__list-item-header-title">
                <span class="pf-v6-screen-reader">Success notification:</span>
                Read success notification title
              </h2>
            </div>
            <div class="pf-v6-c-notification-drawer__list-item-action">
              <button
                class="pf-v6-c-menu-toggle pf-m-plain"
                type="button"
                aria-expanded="false"
                aria-label="Menu toggle"
                id="notification-drawer-groups-example-group3-menu-toggle-6"
              >
                <span class="pf-v6-c-menu-toggle__icon">
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
                      d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                    />
                  </svg>
                </span>
              </button>
            </div>
            <div
              class="pf-v6-c-notification-drawer__list-item-description"
            >This is a success notification description.</div>
            <div
              class="pf-v6-c-notification-drawer__list-item-timestamp"
            >30 minutes ago</div>
          </li>
          <li
            class="pf-v6-c-notification-drawer__list-item pf-m-read pf-m-success pf-m-hoverable"
          >
            <div class="pf-v6-c-notification-drawer__list-item-header">
              <span class="pf-v6-c-notification-drawer__list-item-header-icon">
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
              </span>
              <h2
                class="pf-v6-c-notification-drawer__list-item-header-title pf-m-truncate"
              >
                <span class="pf-v6-screen-reader">Success notification:</span>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent quis odio risus. Ut dictum vitae sapien at posuere. Nullam suscipit massa quis lacus pellentesque scelerisque. Donec non maximus neque, quis ornare nunc. Vivamus in nibh sed libero feugiat feugiat. Nulla lacinia rutrum est, a commodo odio vestibulum suscipit. Nullam id quam et quam porttitor interdum quis nec tellus. Vestibulum arcu dui, pulvinar eu tellus in, semper mattis diam. Sed commodo tincidunt lacus non pulvinar. Curabitur tempor molestie vestibulum. Vivamus vel mi dignissim, efficitur neque eget, efficitur massa. Mauris vitae nunc augue. Donec augue lorem, malesuada et quam vitae, volutpat mattis nisi. Nullam nec venenatis ex, quis lobortis purus. Sed nisl dolor, mattis sit amet tincidunt quis, mollis sed massa.
              </h2>
            </div>
            <div class="pf-v6-c-notification-drawer__list-item-action">
              <button
                class="pf-v6-c-menu-toggle pf-m-plain"
                type="button"
                aria-expanded="false"
                aria-label="Menu toggle"
                id="notification-drawer-groups-example-group3-menu-toggle-7"
              >
                <span class="pf-v6-c-menu-toggle__icon">
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
                      d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                    />
                  </svg>
                </span>
              </button>
            </div>
            <div
              class="pf-v6-c-notification-drawer__list-item-description"
            >This example uses ".pf-m-truncate" to limit the title to a single line and truncate any overflow text with ellipses.</div>
            <div
              class="pf-v6-c-notification-drawer__list-item-timestamp"
            >40 minutes ago</div>
          </li>
          <li
            class="pf-v6-c-notification-drawer__list-item pf-m-read pf-m-success pf-m-hoverable"
          >
            <div class="pf-v6-c-notification-drawer__list-item-header">
              <span class="pf-v6-c-notification-drawer__list-item-header-icon">
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
              </span>
              <h2
                class="pf-v6-c-notification-drawer__list-item-header-title pf-m-truncate"
                style="--pf-v6-c-notification-drawer__list-item-header-title--max-lines: 2"
              >
                <span class="pf-v6-screen-reader">Success notification:</span>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent quis odio risus. Ut dictum vitae sapien at posuere. Nullam suscipit massa quis lacus pellentesque scelerisque. Donec non maximus neque, quis ornare nunc. Vivamus in nibh sed libero feugiat feugiat. Nulla lacinia rutrum est, a commodo odio vestibulum suscipit. Nullam id quam et quam porttitor interdum quis nec tellus. Vestibulum arcu dui, pulvinar eu tellus in, semper mattis diam. Sed commodo tincidunt lacus non pulvinar. Curabitur tempor molestie vestibulum. Vivamus vel mi dignissim, efficitur neque eget, efficitur massa. Mauris vitae nunc augue. Donec augue lorem, malesuada et quam vitae, volutpat mattis nisi. Nullam nec venenatis ex, quis lobortis purus. Sed nisl dolor, mattis sit amet tincidunt quis, mollis sed massa.
              </h2>
            </div>
            <div class="pf-v6-c-notification-drawer__list-item-action">
              <button
                class="pf-v6-c-menu-toggle pf-m-plain"
                type="button"
                aria-expanded="false"
                aria-label="Menu toggle"
                id="notification-drawer-groups-example-group3-menu-toggle-8"
              >
                <span class="pf-v6-c-menu-toggle__icon">
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
                      d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                    />
                  </svg>
                </span>
              </button>
            </div>
            <div
              class="pf-v6-c-notification-drawer__list-item-description"
            >This example uses ".pf-m-truncate" and sets "--pf-v6-c-notification-drawer__list-item-header-title--max-lines: 2" to limit title to two lines and truncate any overflow text with ellipses.</div>
            <div
              class="pf-v6-c-notification-drawer__list-item-timestamp"
            >50 minutes ago</div>
          </li>
          <li
            class="pf-v6-c-notification-drawer__list-item pf-m-read pf-m-success"
          >
            <div class="pf-v6-c-notification-drawer__list-item-header">
              <span class="pf-v6-c-notification-drawer__list-item-header-icon">
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
              </span>
              <h2 class="pf-v6-c-notification-drawer__list-item-header-title">
                <span class="pf-v6-screen-reader">Success notification:</span>
                Notification drawer item title
              </h2>
            </div>
            <div
              class="pf-v6-c-notification-drawer__list-item-action pf-m-no-offset"
            >
              <button class="pf-v6-c-button pf-m-primary" type="button">
                <span class="pf-v6-c-button__text">Action</span>
              </button>
            </div>
            <div
              class="pf-v6-c-notification-drawer__list-item-description"
            >This example uses ".pf-m-no-offset" on the action wrapper to disable the default offset for button alignment.</div>
            <div
              class="pf-v6-c-notification-drawer__list-item-timestamp"
            >55 minutes ago</div>
          </li>
        </ul>
      </section>
      <section class="pf-v6-c-notification-drawer__group">
        <h1>
          <button
            class="pf-v6-c-notification-drawer__group-toggle"
            aria-expanded="false"
          >
            <div
              class="pf-v6-c-notification-drawer__group-toggle-title"
            >Fourth notification group</div>
            <div class="pf-v6-c-notification-drawer__group-toggle-count">
              <span class="pf-v6-c-badge pf-m-unread">2</span>
            </div>
            <span class="pf-v6-c-notification-drawer__group-toggle-icon">
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
          </button>
        </h1>
        <ul class="pf-v6-c-notification-drawer__list" role="list" hidden>
          <li
            class="pf-v6-c-notification-drawer__list-item pf-m-hoverable pf-m-info"
            tabindex="0"
          >
            <div class="pf-v6-c-notification-drawer__list-item-header">
              <span class="pf-v6-c-notification-drawer__list-item-header-icon">
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
              </span>
              <h2 class="pf-v6-c-notification-drawer__list-item-header-title">
                <span class="pf-v6-screen-reader">Info notification:</span>
                Unread
                info notification title
              </h2>
            </div>
            <div class="pf-v6-c-notification-drawer__list-item-action">
              <button
                class="pf-v6-c-menu-toggle pf-m-plain"
                type="button"
                aria-expanded="false"
                aria-label="Menu toggle"
                id="notification-drawer-groups-example-group4-menu-toggle-1"
              >
                <span class="pf-v6-c-menu-toggle__icon">
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
                      d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                    />
                  </svg>
                </span>
              </button>
            </div>
            <div
              class="pf-v6-c-notification-drawer__list-item-description"
            >This is an info notification description.</div>
            <div
              class="pf-v6-c-notification-drawer__list-item-timestamp"
            >5 minutes ago</div>
          </li>

          <li
            class="pf-v6-c-notification-drawer__list-item pf-m-hoverable pf-m-custom"
            tabindex="0"
          >
            <div class="pf-v6-c-notification-drawer__list-item-header">
              <span class="pf-v6-c-notification-drawer__list-item-header-icon">
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
              <h2 class="pf-v6-c-notification-drawer__list-item-header-title">
                <span class="pf-v6-screen-reader">Custom notification:</span>
                Unread
                recommendation notification title. This is a long title to show how the title will wrap if it is long and wraps to multiple lines.
              </h2>
            </div>
            <div class="pf-v6-c-notification-drawer__list-item-action">
              <button
                class="pf-v6-c-menu-toggle pf-m-plain"
                type="button"
                aria-expanded="false"
                aria-label="Menu toggle"
                id="notification-drawer-groups-example-group4-menu-toggle-3"
              >
                <span class="pf-v6-c-menu-toggle__icon">
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
                      d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                    />
                  </svg>
                </span>
              </button>
            </div>
            <div
              class="pf-v6-c-notification-drawer__list-item-description"
            >This is a recommendation notification description. This is a long description to show how the title will wrap if it is long and wraps to multiple lines.</div>
            <div
              class="pf-v6-c-notification-drawer__list-item-timestamp"
            >10 minutes ago</div>
          </li>

          <li
            class="pf-v6-c-notification-drawer__list-item pf-m-hoverable pf-m-custom"
            tabindex="0"
          >
            <div class="pf-v6-c-notification-drawer__list-item-header">
              <span class="pf-v6-c-notification-drawer__list-item-header-icon">
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
              <h2 class="pf-v6-c-notification-drawer__list-item-header-title">
                <span class="pf-v6-screen-reader">Custom notification:</span>
                Unread
                recommendation notification title. This is a long title to show how the title will wrap if it is long and wraps to multiple lines.
              </h2>
            </div>
            <div class="pf-v6-c-notification-drawer__list-item-action">
              <button
                class="pf-v6-c-menu-toggle pf-m-plain"
                type="button"
                aria-expanded="false"
                aria-label="Menu toggle"
                id="notification-drawer-groups-example-group4-menu-toggle-4"
              >
                <span class="pf-v6-c-menu-toggle__icon">
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
                      d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                    />
                  </svg>
                </span>
              </button>
            </div>
            <div
              class="pf-v6-c-notification-drawer__list-item-description"
            >This is a recommendation notification description. This is a long description to show how the title will wrap if it is long and wraps to multiple lines.</div>
            <div
              class="pf-v6-c-notification-drawer__list-item-timestamp"
            >20 minutes ago</div>
          </li>
          <li
            class="pf-v6-c-notification-drawer__list-item pf-m-read pf-m-warning pf-m-hoverable"
          >
            <div class="pf-v6-c-notification-drawer__list-item-header">
              <span class="pf-v6-c-notification-drawer__list-item-header-icon">
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
              </span>
              <h2 class="pf-v6-c-notification-drawer__list-item-header-title">
                <span class="pf-v6-screen-reader">Warning notification:</span>
                Read warning notification title
              </h2>
            </div>
            <div class="pf-v6-c-notification-drawer__list-item-action">
              <button
                class="pf-v6-c-menu-toggle pf-m-plain"
                type="button"
                aria-expanded="false"
                aria-label="Menu toggle"
                id="notification-drawer-groups-example-group4-menu-toggle-5"
              >
                <span class="pf-v6-c-menu-toggle__icon">
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
                      d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                    />
                  </svg>
                </span>
              </button>
            </div>
            <div
              class="pf-v6-c-notification-drawer__list-item-description"
            >This is a warning notification description.</div>
            <div
              class="pf-v6-c-notification-drawer__list-item-timestamp"
            >20 minutes ago</div>
          </li>
          <li
            class="pf-v6-c-notification-drawer__list-item pf-m-read pf-m-success pf-m-hoverable"
          >
            <div class="pf-v6-c-notification-drawer__list-item-header">
              <span class="pf-v6-c-notification-drawer__list-item-header-icon">
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
              </span>
              <h2 class="pf-v6-c-notification-drawer__list-item-header-title">
                <span class="pf-v6-screen-reader">Success notification:</span>
                Read success notification title
              </h2>
            </div>
            <div class="pf-v6-c-notification-drawer__list-item-action">
              <button
                class="pf-v6-c-menu-toggle pf-m-plain"
                type="button"
                aria-expanded="false"
                aria-label="Menu toggle"
                id="notification-drawer-groups-example-group4-menu-toggle-6"
              >
                <span class="pf-v6-c-menu-toggle__icon">
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
                      d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                    />
                  </svg>
                </span>
              </button>
            </div>
            <div
              class="pf-v6-c-notification-drawer__list-item-description"
            >This is a success notification description.</div>
            <div
              class="pf-v6-c-notification-drawer__list-item-timestamp"
            >30 minutes ago</div>
          </li>
          <li
            class="pf-v6-c-notification-drawer__list-item pf-m-read pf-m-success pf-m-hoverable"
          >
            <div class="pf-v6-c-notification-drawer__list-item-header">
              <span class="pf-v6-c-notification-drawer__list-item-header-icon">
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
              </span>
              <h2
                class="pf-v6-c-notification-drawer__list-item-header-title pf-m-truncate"
              >
                <span class="pf-v6-screen-reader">Success notification:</span>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent quis odio risus. Ut dictum vitae sapien at posuere. Nullam suscipit massa quis lacus pellentesque scelerisque. Donec non maximus neque, quis ornare nunc. Vivamus in nibh sed libero feugiat feugiat. Nulla lacinia rutrum est, a commodo odio vestibulum suscipit. Nullam id quam et quam porttitor interdum quis nec tellus. Vestibulum arcu dui, pulvinar eu tellus in, semper mattis diam. Sed commodo tincidunt lacus non pulvinar. Curabitur tempor molestie vestibulum. Vivamus vel mi dignissim, efficitur neque eget, efficitur massa. Mauris vitae nunc augue. Donec augue lorem, malesuada et quam vitae, volutpat mattis nisi. Nullam nec venenatis ex, quis lobortis purus. Sed nisl dolor, mattis sit amet tincidunt quis, mollis sed massa.
              </h2>
            </div>
            <div class="pf-v6-c-notification-drawer__list-item-action">
              <button
                class="pf-v6-c-menu-toggle pf-m-plain"
                type="button"
                aria-expanded="false"
                aria-label="Menu toggle"
                id="notification-drawer-groups-example-group4-menu-toggle-7"
              >
                <span class="pf-v6-c-menu-toggle__icon">
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
                      d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                    />
                  </svg>
                </span>
              </button>
            </div>
            <div
              class="pf-v6-c-notification-drawer__list-item-description"
            >This example uses ".pf-m-truncate" to limit the title to a single line and truncate any overflow text with ellipses.</div>
            <div
              class="pf-v6-c-notification-drawer__list-item-timestamp"
            >40 minutes ago</div>
          </li>
          <li
            class="pf-v6-c-notification-drawer__list-item pf-m-read pf-m-success pf-m-hoverable"
          >
            <div class="pf-v6-c-notification-drawer__list-item-header">
              <span class="pf-v6-c-notification-drawer__list-item-header-icon">
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
              </span>
              <h2
                class="pf-v6-c-notification-drawer__list-item-header-title pf-m-truncate"
                style="--pf-v6-c-notification-drawer__list-item-header-title--max-lines: 2"
              >
                <span class="pf-v6-screen-reader">Success notification:</span>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent quis odio risus. Ut dictum vitae sapien at posuere. Nullam suscipit massa quis lacus pellentesque scelerisque. Donec non maximus neque, quis ornare nunc. Vivamus in nibh sed libero feugiat feugiat. Nulla lacinia rutrum est, a commodo odio vestibulum suscipit. Nullam id quam et quam porttitor interdum quis nec tellus. Vestibulum arcu dui, pulvinar eu tellus in, semper mattis diam. Sed commodo tincidunt lacus non pulvinar. Curabitur tempor molestie vestibulum. Vivamus vel mi dignissim, efficitur neque eget, efficitur massa. Mauris vitae nunc augue. Donec augue lorem, malesuada et quam vitae, volutpat mattis nisi. Nullam nec venenatis ex, quis lobortis purus. Sed nisl dolor, mattis sit amet tincidunt quis, mollis sed massa.
              </h2>
            </div>
            <div class="pf-v6-c-notification-drawer__list-item-action">
              <button
                class="pf-v6-c-menu-toggle pf-m-plain"
                type="button"
                aria-expanded="false"
                aria-label="Menu toggle"
                id="notification-drawer-groups-example-group4-menu-toggle-8"
              >
                <span class="pf-v6-c-menu-toggle__icon">
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
                      d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                    />
                  </svg>
                </span>
              </button>
            </div>
            <div
              class="pf-v6-c-notification-drawer__list-item-description"
            >This example uses ".pf-m-truncate" and sets "--pf-v6-c-notification-drawer__list-item-header-title--max-lines: 2" to limit title to two lines and truncate any overflow text with ellipses.</div>
            <div
              class="pf-v6-c-notification-drawer__list-item-timestamp"
            >50 minutes ago</div>
          </li>
          <li
            class="pf-v6-c-notification-drawer__list-item pf-m-read pf-m-success"
          >
            <div class="pf-v6-c-notification-drawer__list-item-header">
              <span class="pf-v6-c-notification-drawer__list-item-header-icon">
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
              </span>
              <h2 class="pf-v6-c-notification-drawer__list-item-header-title">
                <span class="pf-v6-screen-reader">Success notification:</span>
                Notification drawer item title
              </h2>
            </div>
            <div
              class="pf-v6-c-notification-drawer__list-item-action pf-m-no-offset"
            >
              <button class="pf-v6-c-button pf-m-primary" type="button">
                <span class="pf-v6-c-button__text">Action</span>
              </button>
            </div>
            <div
              class="pf-v6-c-notification-drawer__list-item-description"
            >This example uses ".pf-m-no-offset" on the action wrapper to disable the default offset for button alignment.</div>
            <div
              class="pf-v6-c-notification-drawer__list-item-timestamp"
            >55 minutes ago</div>
          </li>
        </ul>
      </section>
    </div>
  </div>
</div>

```

### Accessibility

| Attribute | Applied to | Outcome |
| -- | -- | -- |
| `aria-expanded="false"` | `.pf-v6-c-notification-drawer__group-toggle` | Indicates that the group notification list is hidden. |
| `aria-expanded="true"` | `.pf-v6-c-notification-drawer__group-toggle` | Indicates that the group notification list is visible. |
| `hidden` | `.pf-v6-c-notification-drawer__list` | Indicates that the group notification list is hidden so that it isn't visible in the UI and isn't accessed by assistive technologies. |
| `tabindex="0"` | `.pf-v6-c-notification-drawer__list-item.pf-m-hoverable` | Inserts the hoverable list item into the tab order of the page so that it is focusable. |
| `aria-hidden="true"` | `.pf-v6-c-notification-drawer__group-toggle-icon > *`, `.pf-v6-c-notification-drawer__list-item-header-icon > *` | Hides icon for assistive technologies. |

### Usage

| Class | Applied to | Outcome |
| -- | -- | -- |
| `.pf-v6-c-notification-drawer` | `<div>` | Initiates the notification drawer. **Required** |
| `.pf-v6-c-notification-drawer__header` | `<div>` | Initiates the notification drawer header. **Required** |
| `.pf-v6-c-notification-drawer__header-title` | `<h1>` | Initiates the notification drawer header title. **Required** |
| `.pf-v6-c-notification-drawer__header-status` | `<span>` | Initiates the notification drawer header status. |
| `.pf-v6-c-notification-drawer__header-action` | `<div>` | Initiates the notification drawer header action. |
| `.pf-v6-c-notification-drawer__header-action-close` | `<div>` | Initiates the notification drawer header action button. |
| `.pf-v6-c-notification-drawer__body` | `<div>` | Initiates the notification drawer body. **Required** |
| `.pf-v6-c-notification-drawer__list` | `<ul>` | Initiates a notification list. **Required** |
| `.pf-v6-c-notification-drawer__list-item` | `<li>` | Initiates a notification list item. Always use with a state modifier class. **Required** |
| `.pf-v6-c-notification-drawer__list-item-header` | `<div>` | Initiates a notification list item header. **Required** |
| `.pf-v6-c-notification-drawer__list-item-header-icon` | `<span>` | Initiates a notification list item header icon. **Required** |
| `.pf-v6-c-notification-drawer__list-item-header-title` | `<h2>` | Initiates a notification list item header title. **Required** |
| `.pf-v6-c-notification-drawer__list-item-action` | `<div>` | Initiates a notification list item action. |
| `.pf-v6-c-notification-drawer__list-item-description` | `<div>` | Initiates a notification list item description. **Required** |
| `.pf-v6-c-notification-drawer__list-item-timestamp` | `<div>` | Initiates a notification list item timestamp. **Required** |
| `.pf-v6-c-notification-drawer__group-list` | `<div>` | Initiates a notification group list. **Required when notifications are grouped** |
| `.pf-v6-c-notification-drawer__group` | `<section>` | Initiates a notification group. **Required** |
| `.pf-v6-c-notification-drawer__group-toggle` | `<button>` | Initiates a notification group toggle. **Required** |
| `.pf-v6-c-notification-drawer__group-title` | `<div>` | Initiates a notification group toggle title. **Required** |
| `.pf-v6-c-notification-drawer__group-count` | `<div>` | Initiates a notification group toggle count. |
| `.pf-v6-c-notification-drawer__group-icon` | `<span>` | Initiates a notification group toggle icon. **Required** |
| `.pf-m-custom` | `.pf-v6-c-notification-drawer__list-item` | Modifies a notification list item for the custom state. |
| `.pf-m-info` | `.pf-v6-c-notification-drawer__list-item` | Modifies a notification list item for the info state. |
| `.pf-m-warning` | `.pf-v6-c-notification-drawer__list-item` | Modifies a notification list item for the warning state. |
| `.pf-m-danger` | `.pf-v6-c-notification-drawer__list-item` | Modifies a notification list item for the danger state. |
| `.pf-m-success` | `.pf-v6-c-notification-drawer__list-item` | Modifies a notification list item for the success state. |
| `.pf-m-read` | `.pf-v6-c-notification-drawer__list-item` | Modifies a notification list item for the read state. |
| `.pf-m-hoverable` | `.pf-v6-c-notification-drawer__list-item` | Modifies a notification list item hover states to inidicate it is clickable. |
| `.pf-m-expanded` | `.pf-v6-c-notification-drawer__group` | Modifies a notification group for the expanded state. |
| `.pf-m-truncate` | `.pf-v6-c-notification-drawer__list-item-header-title` |  Modifies the title to display a single line and truncate any overflow text with ellipses. **Note:** you can specify the max number of lines to show by setting the `--pf-v6-c-notification-drawer__list-item-header-title--max-lines` (the default value is `1`). |
| `.pf-m-no-offset` | `.pf-v6-c-notification-drawer__list-item-action` | Modifies a notification item action to remove the vertical offset for action alignment. |
