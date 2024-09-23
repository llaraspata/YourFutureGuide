import { ChangeDetectionStrategy, Component, ElementRef, ViewChild } from '@angular/core';
import { MatCardModule } from '@angular/material/card';
import { Message } from './Message';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { LlmMessage } from './LlmMessage';


@Component({
  selector: 'app-chat',
  standalone: true,
  imports: [MatCardModule, HttpClientModule],
  templateUrl: './chat.component.html',
  styleUrl: './chat.component.css',
  changeDetection: ChangeDetectionStrategy.OnPush,
})


export class ChatComponent {
  @ViewChild("message", { static: false }) message?: ElementRef;

  chatMessagesUI: Message[] = [];
  chatMessagesLLM: LlmMessage[] = [];
  order = 0;

  rootYFG = "http://127.0.0.1:8000/"
  degreePredictionApi = "http://127.0.0.1:8000/predict/degree"
  careerPredictionApi = "http://127.0.0.1:8000/predict/career"

  isWriting = false;


  constructor(private http: HttpClient) {
    let initialOptions = [
      {
        "id": 0,
        "icon": "📚",
        "content": "La laurea che meglio si allinea alle mie passioni",
        "message": "Vorrei scoprire la laurea che meglio si allinea alle mie passioni"
      },
      {
        "id": 1,
        "icon": "💼",
        "content": "Il percorso professionale perfetto per me",
        "message": "Vorrei scoprire il percorso professionale perfetto per me"
      } 
    ];

    this.chatMessagesUI = [
      {
        "display_order": 1,
        "type": "R", //received
        "content": "Cosa vorresti scoprire?",
        "options": initialOptions
      }
    ];

    this.order = this.chatMessagesUI.length;
  }


  async startConversation(choosenOption: number) {
    this.isWriting = true;

    var apiToCall = "";

    if (choosenOption === 0) {
      apiToCall = this.degreePredictionApi;
    } 
    else if (choosenOption === 1) {
      apiToCall = this.careerPredictionApi;
    }

    this.addChoiseToChat(choosenOption);

    let newMsg = {
      "display_order": this.order++,
      "type": "R",
      "content": "",
      "options": []
    };

    this.postStartConversation(apiToCall).subscribe((response: any) => {
      this.chatMessagesLLM = response.chat_messages;

      console.log(response.llm_output);
      
      newMsg.content = response.llm_output;
      console.log(newMsg.content);

      this.chatMessagesUI.push(newMsg);
      this.isWriting = false;

    });
  }

  addChoiseToChat(choosenOption: number) {

    let newMsg = {
      "display_order": this.order++,
      "type": "S",
      "content": this.chatMessagesUI[0].options[choosenOption].message,
      "options": []
    };

    console.log(choosenOption);


    this.chatMessagesUI.push(newMsg);
  }

  postStartConversation(api: string) {
    const jsonPayload = {
      "usr_answer": "",
      "chat": [],
      "qst_count": 0
    };

    return this.http.post(api, jsonPayload);
  }


  sendMessage() {
    if (!this.message?.nativeElement.value) {
      return;
    }

    let newMsg = {
      "display_order": this.order++,
      "type": "S",
      "content": this.message.nativeElement.value,
      "options": []
    };

    this.chatMessagesUI.push(newMsg);
    this.message.nativeElement.value = "";
  }

  

}
