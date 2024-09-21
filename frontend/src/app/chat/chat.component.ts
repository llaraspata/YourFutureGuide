import { ChangeDetectionStrategy, Component, ElementRef, ViewChild } from '@angular/core';
import { MatCardModule } from '@angular/material/card';
import { Message } from './Message';
import { Option } from './Option';

@Component({
  selector: 'app-chat',
  standalone: true,
  imports: [MatCardModule],
  templateUrl: './chat.component.html',
  styleUrl: './chat.component.css',
  changeDetection: ChangeDetectionStrategy.OnPush,
})


export class ChatComponent {
  @ViewChild("message", { static: false }) message?: ElementRef;

  chatMessages: Message[] = [];
  order = 0;
  newMsg!: Message;

  options!: Option[];


  constructor() {
    this.chatMessages = [
      {
        "display_order": 1,
        "type": "R", //received
        "content": "Cosa vorresti scoprire?"
      },
      {
        "display_order": 2,
        "type": "S", //sent
        "content": "Trovare il corso di laurea che più di addice a me."
      },
      {
        "display_order": 3,
        "type": "R", //received
        "content": "Quali sono le tue principali passioni?"
      }
    ];

    this.order = this.chatMessages.length;

    this.options = [
      {
        "id": 1,
        "icon": "📚",
        "content": "La laurea che meglio si allinea alle mie passioni"
      },
      {
        "id": 2,
        "icon": "💼",
        "content": "Il percorso professionale perfetto per me"
      } 
    ];
    
  }


  sendMessage() {
    if (!this.message?.nativeElement.value) {
      //this.noIdToExtract = true;
      return;
    }

    this.newMsg = {
      "display_order": this.order++,
      "type": "S",
      "content": this.message.nativeElement.value
    };

    this.chatMessages.push(this.newMsg);
    this.message.nativeElement.value = "";
  }

}
